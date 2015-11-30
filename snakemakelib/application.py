# Copyright (C) 2015 by Per Unneberg
import os
import pandas as pd
from blaze import odo
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
            assert isinstance(v[0], IOTarget), "first value must be of instance IOTarget"
            if not v[1] is None:
                assert isinstance(v[1], IOAggregateTarget), "second value must be of instance IOAggregateTarget or None"
        assert isinstance(run, bool), "run must be a boolean"
        self._units = units if units else []
        self._iotargets = iotargets
        self._targets = {}
        self._annotation_funcs = {}
        self._post_processing_hooks = {}
        self._plot_funcs = {}
        self._name = name
        self._aggregate_data = {}
        self._aggregate_targets = {}
        self._annotate = kwargs.get("annotate", False)
        self._run = run


    @property
    def name(self):
        return self._name


    @property
    def iotargets(self):
        return self._iotargets
        

    @property
    def targets(self):
        if not self._run:
            return {k:[] for k in self.iotargets.keys()}
        if not self._targets:
            self._make_targets()
        return self._targets
        
            
    def _make_targets(self):
        for k,v in self.iotargets.items():
            self._targets[k] = [v[0].format(**u) for u in self.units]
            

    @property
    def aggregate_targets(self):
        if not self._run:
            return {k:[] for k in self.iotargets.keys()}
        if not self._aggregate_targets:
            self._make_aggregate_targets()
        return self._aggregate_targets


    def _make_aggregate_targets(self):
        for k,v in self.iotargets.items():
            self._aggregate_targets[k] = v[1].format()

            
    def aggregate(self, key=None):
        for k in self.targets.keys():
            if not key is None and not key == k:
                next
            annotate = self._annotate
            if not self._annotation_funcs.get(k, None) is None:
                smllogger.debug("Annotating data")
                annotate = True
            df = pd.concat([
                odo(x, pd.DataFrame,
                    annotate=annotate,
                    annotation_fn=self._annotation_funcs.get(k, None)) for x in self.targets[k]
            ])
            # Run post-processing hooks, if any
            if not self._post_processing_hooks.get(k, None) is None:
                smllogger.debug("Running post processing hook")
                df = self._post_processing_hooks[k](df)
            self._aggregate_data[k] = df

    @property
    def aggregate_data(self):
        return self._aggregate_data
            
    def set_units(self, units):
        self._units = units
        self._make_targets()


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


    def plot(self, plotkey=None, **kwargs):
        """For each aggregation key, return list of plots"""
        d = {}
        for key in self.aggregate_data.keys():
            if not plotkey is None:
                if plotkey != key:
                    continue
            df = self.aggregate_data[key]
            d[key] = []
            if not self._plot_funcs.get(key, None) is None:
                d[key] = [f(df, **kwargs) for f in self._plot_funcs[key]]
        return d
    
        
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
                    df['PlatformUnit'] = df[samplekey] + "__" + df[pukey]
                except AttributeError:
                    raise
                return df
            return _annotate_fn
        
        for k in self.iotargets.keys():
            self._annotation_funcs[k] = _annotate_fn_factory(self.iotargets[k][0])
