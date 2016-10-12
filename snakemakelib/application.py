""" Container classes for applications.

"""
import os
import pandas as pd
from blaze import odo
from bokeh.plotting import figure
from .io import IOTarget, IOAggregateTarget
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

class Application(object):
    """Container class for an application.

    NB: this is still WIP and it is likely that this class should be
    split into several subclasses, and/or be implemented as a
    meta-class.

    An application in this context is more or less equivalent to a
    rule in the snakemake workflow. The Application class has
    functionality to

    1. generate target names
    2. collect data output via odo
    3. plot results
    4. configuration options, e.g. for running

    """

    def __init__(self, name, iotargets, units=None, run=True, **kwargs):
        assert isinstance(iotargets, dict), "iotargets must be a dictionary"
        assert len(iotargets.items()) > 0, "iotargets must not be empty"
        for k,v in iotargets.items():
            assert isinstance(v, tuple), "iotargets values must be a tuple"
            assert len(v) == 2, "iotargets values must be of length 2"
            if not v[0] is None:
                assert isinstance(v[0], IOTarget), "first value must be of instance IOTarget or None"
            if not v[1] is None:
                assert isinstance(v[1], IOAggregateTarget), "second value must be of instance IOAggregateTarget or None"
            if v[0] is None and v[1] is None:
                raise Exception("first and second value cannot both be None")
        assert isinstance(run, bool), "run must be a boolean"
        self._units = units if units else []
        self._iotargets = iotargets
        self._targets = {}
        self._annotation_funcs = {}
        self._post_processing_hooks = {}
        self._aggregate_post_processing_hooks = {}
        self._plot_funcs = {}
        self._name = name
        self._aggregate_data = {}
        self._aggregate_targets = {}
        self._annotate = kwargs.get("annotate", False)
        self._run = run


    @property
    def run(self):
        """Variable that states whether the application is run or not.

        Returns:
          bool:
        """
        return self._run

        
    @property
    def name(self):
        """Get the application name.

        Returns:
          str:
            application name
        """
        return self._name


    @property
    def iotargets(self):
        """Get the application input/output (io) targets.

        Returns:
          dict:
            Returns a dictionary where keys correspond to
            groups of targets and values lists
            :class:`snakemakelib.io.IOTarget` objects.

        """
        return self._iotargets
        

    @property
    def targets(self):
        """Get the application targets, which is a list of snakemake target
        names. If list is empty, try to create targets.

        Returns:
          dict:
            key-value mapping where keys correspond to groups of targets, values to lists of snakemake target names
        """
        if not self._run:
            return {k:[] for k in self.iotargets.keys()}
        if not self._targets:
            self._make_targets()
        return self._targets
        
            
    def _make_targets(self):
        """Create targets from iotargets.

        Returns:
          None:
        """
        for k,v in self.iotargets.items():
            if v[0]:
                self._targets[k] = list(set([v[0].format(**u) for u in self.units]))
            # Initialize aggregate_data, even if no target is defined
            self._aggregate_data[k] = None
            

    @property
    def aggregate_targets(self):
        """Aggregate targets and return results.

        Returns:
          dict:
            key value mapping where keys correspond to application groups, values to :class:`snakemakelib.io.IOTarget` objects
        """
        if not self._run:
            return {k:[] for k in self.iotargets.keys()}
        if not self._aggregate_targets:
            self._make_aggregate_targets()
        return self._aggregate_targets


    def _make_aggregate_targets(self):
        """Utility function to create aggregate targets.
        """
        for k,v in self.iotargets.items():
            if v[1] is None:
                self._aggregate_targets[k] = []
            else:
                self._aggregate_targets[k] = v[1].format()

            
    def aggregate(self, key=None, **kwargs):
        """Aggregate targets to aggregate_targets, if present.

        Args:
          key (str): aggregate targets for key, if None all targets are aggregated
          kwargs (dict): additional arguments, passed to *all* hooks

        """

        if not self.run:
            return self
        for k,v in self.iotargets.items():
            smllogger.debug("Aggregating key {}, iotargets: {}".format(k, v))
            if not key is None and not key == k:
                continue
            if self.iotargets[k][1] is None:
                smllogger.debug("Skipping iotarget key ", k)
                continue
            annotate = self._annotate
            if not self._annotation_funcs.get(k, None) is None:
                smllogger.debug("Annotating data")
                annotate = True
            try:
                dflist = [
                    odo(x, pd.DataFrame,
                        annotate=annotate,
                        annotation_fn=self._annotation_funcs.get(k, None), key=k, **kwargs) for x in self.targets[k]
                ]
            except:
                smllogger.warn("Unable to generate data frame list; not aggregating results for targets {}".format(self.targets[k]))
                return self
            # Run post-processing hooks, if any
            if not self._post_processing_hooks.get(k, None) is None:
                smllogger.debug("Running post processing hook")
                dflist = [self._post_processing_hooks[k](df, **kwargs) for df in dflist]
            df = pd.concat(dflist)
            # Run post-processing hook for aggregated data, if any
            if not self._aggregate_post_processing_hooks.get(k, None) is None:
                smllogger.debug("Running post processing hook on aggregated data")
                df = self._aggregate_post_processing_hooks[k](df, **kwargs)
            self._aggregate_data[k] = df
        return self
    

    @property
    def aggregate_data(self):
        return self._aggregate_data


    def filter_aggregate_data(self, datakey, key=None, values=None):
        if values is None:
            return
        if key is None:
            return
        try:
            self._aggregate_data[datakey] = self._aggregate_data[datakey][self._aggregate_data[datakey][key].isin(values)]
        except:
            raise Exception("failed to filter aggregate data on datakey {}, key {} using values {}".format(datakey, key, values))
        return
    

    def set_units(self, units):
        self._units = units
        self._make_targets()
        return self


    @property
    def units(self):
        return self._units


    def register_annotation_fn(self, key):
        """Decorator for registering annotation functions"""
        def wrap(func):
            self.add_annotation_fn(func, key)
            return func
        return wrap


    def add_annotation_fn(self, func, key):
        self._annotation_funcs[key] = func


    def register_post_processing_hook(self, key):
        """Decorator for registering post processing hook.

        Sometimes the data needs to be transformed in some way, e.g.
        pivoted into wide format. This decorator registers a post
        processing hook that is run once the data has been read.

        """
        def wrap(func):
            self.add_post_processing_hook(func, key)
            return func
        return wrap


    def add_post_processing_hook(self, func, key):
        self._post_processing_hooks[key] = func


    def register_aggregate_post_processing_hook(self, key):
        """Decorator for registering post processing hook to be run on
        aggregate data.

        Sometimes the data needs to be transformed in some way, e.g.
        pivoted into wide format. This decorator registers a post
        processing hook that is run on the aggregated data.

        """
        def wrap(func):
            self.add_aggregate_post_processing_hook(func, key)
            return func
        return wrap


    def add_aggregate_post_processing_hook(self, func, key):
        self._aggregate_post_processing_hooks[key] = func

        
    def register_plot(self, key):
        """Decorator for registering plot"""

        def wrap(func):
            self.add_plot_func(func, key)
            return func
        return wrap


    def add_plot_func(self, func, key):
        if not key in self._plot_funcs:
            self._plot_funcs[key] = [func]
        else:
            self._plot_funcs[key].append(func)


    def reset_plot_func(self, key):
        """Remove plotting functions for a key"""
        self._plot_funcs[key] = []


    def plot(self, key, **kwargs):
        """Create plots for plotkey."""
        df = self.aggregate_data[key]
        if not self._plot_funcs.get(key, None) is None:
            return [f(df, **kwargs) for f in self._plot_funcs[key]]
        return
    

    def save_aggregate_data(self, datakey=None, backend="csv", **kwargs):
        """Save aggregate data"""
        for key in self.aggregate_data.keys():
            if self.iotargets[key][1] is None:
                continue
            if self.aggregate_data[key] is None:
                # Emulate touch so rule completes
                with open(self.iotargets[key][1], "w") as fh:
                    fh.write("")
                continue
            if not datakey is None:
                if datakey != key:
                    continue
            if backend == "csv":
                index = kwargs.pop('index', False)
                self.aggregate_data[key].reset_index().to_csv(self.aggregate_targets[key], index=index, **kwargs)
            # FIXME: all hdf5 data should go to same output; would
            # need to write text to aggregate_targets[key] so target
            # has been created
            # elif backend == "hdf5":
            #     self.aggregate_data[key].to_hdf(self.aggregate_targets[key], key=key)
            # elif backend == "sql":
            #     self.aggregate_data[key].to_sql(self.aggregate_targets[key], key=key, con=kwargs.get(con, None))
            else:
                raise Exception("Unsupported backend ", backend)


    def read_aggregate_data(self, datakey=None, backend="csv", **kwargs):
        """Read aggregate data"""
        for key in self.iotargets.keys():
            if self.iotargets[key][1] is None:
                continue
            if not datakey is None:
                if datakey != key:
                    continue
            if backend == "csv":
                try:
                    self.aggregate_data[key] = pd.read_csv(self.aggregate_targets[key], **kwargs)
                except:
                    smllogger.warn("Failed to read aggregate data for {}".format(self.aggregate_targets[key]))


    def __str__(self):
        return repr(self) + "; application name: " + self.name
    


class SampleApplication(Application):

    """SampleApplication class

    Automagically adds annotation function that annotates data frames
    by sample unit.
    """
    def __init__(self, samplekey="SM", **kwargs):
        super(SampleApplication, self).__init__(**kwargs)
        def _annotate_fn_factory(iotarget, **kwargs):
            def _annotate_fn(df, uri, **kwargs):
                m = iotarget.search(uri)
                try:
                    df[samplekey] = iotarget.concat_groupdict[samplekey]
                    df[samplekey] = df[samplekey].astype(str)
                    df.set_index([samplekey], append=True, inplace=True)
                except KeyError:
                    raise
                except AttributeError:
                    raise
                return df
            return _annotate_fn
        
        for k in self.iotargets.keys():
            self._annotation_funcs[k] = _annotate_fn_factory(self.iotargets[k][0])



class PlatformUnitApplication(Application):
    """PlatformUnitApplication class

    Automagically adds annotation function that annotates data frames
    by sample and platform unit (i.e. run level)
    """
    def __init__(self, samplekey="SM", pukey="PU", **kwargs):
        super(PlatformUnitApplication, self).__init__(**kwargs)
        def _annotate_fn_factory(iotarget, **kwargs):
            def _annotate_fn(df, uri, **kwargs):
                m = iotarget.search(uri)
                try:
                    df[samplekey] = iotarget.concat_groupdict[samplekey]
                    df[pukey] = iotarget.concat_groupdict[pukey]
                    df[samplekey] = df[samplekey].astype(str)
                    df[pukey] = df[pukey].astype(str)
                    df['PlatformUnit'] = df[samplekey] + "__" + df[pukey]
                except KeyError:
                    smllogger.warn("No platform unit present; using sample unit to identify platform unit")
                    df[pukey] = iotarget.concat_groupdict[samplekey]
                    df[pukey] = df[samplekey].astype(str)
                    df['PlatformUnit'] = df[samplekey] + "__" + df[pukey]
                except AttributeError:
                    raise
                return df
            return _annotate_fn
        
        for k in self.iotargets.keys():
            self._annotation_funcs[k] = _annotate_fn_factory(self.iotargets[k][0])
