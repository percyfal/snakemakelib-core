# Copyright (C) 2015 by Per Unneberg
import pandas as pd
from blaze import odo
from .io import IOTarget, IOAggregateTarget

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
        if not self._targets:
            self._make_targets()
        return self._targets
        
            
    def _make_targets(self):
        for k,v in self.iotargets.items():
            self._targets[k] = [v[0].format(**u) for u in self.units]
            

    @property
    def aggregate_targets(self):
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
                annotate = True
            df = pd.concat([
                odo(x, pd.DataFrame,
                    annotate=annotate,
                    annotation_fn=self._annotation_funcs.get(k, None)) for x in self.targets[k]
            ])
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
        def _(func):
            self.add_annotation_fn(func, key)
            return func
        return _


    def add_annotation_fn(self, func, key):
        self._annotation_funcs[key] = func


    def __str__(self):
        return repr(self) + "; application name: " + self.name
    


class SampleApplication(Application):
    """SampleApplication class

    Automagically adds annotation function that annotates data frames
    by sample key.
    """
    pass
