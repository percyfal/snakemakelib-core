# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
import os
import logging
import pytest
import pandas as pd
from blaze import DataFrame, resource
from ..application import Application
from ..io import IOTarget, IOSampleTarget, IOAggregateTarget
logging.basicConfig(level=logging.DEBUG)
from snakemakelib.odo import pandas

@resource.register('.+\.foo')
def resource_foo_to_df(uri, annotate=False, **kwargs):
    df = pd.read_csv(uri)
    if annotate:
        df = pandas.annotate_by_uri(df, uri, **kwargs)
    return df


@pytest.fixture(scope="module")
def foo1(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo1_bar1.foo')
    fn.write("""foo,bar\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def foo2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo2_bar2.foo')
    fn.write("""foo,bar\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def foo3(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo3_bar3.foo')
    fn.write("""foo,bar\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def bar1(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('bar1_foo1.foo')
    fn.write("""bar,foo\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def bar2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('bar2_foo2.foo')
    fn.write("""bar,foo\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def bar3(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('bar3_foo3.foo')
    fn.write("""bar,foo\n1,2\n3,4""")
    return fn



class TestApplication:
    """Test application class"""
    units = [
        {'foo': 'foo1', 'bar': 'bar1'},
        {'foo': 'foo2', 'bar': 'bar2'},
        {'foo': 'foo3', 'bar': 'bar3'}
    ]
    iotargets = {'foo':(IOTarget("{foo}_{bar}"), None)}
    iotargets_w_suffix = {'foo':(IOTarget("{foo}_{bar}", suffix=".foo"), None)}
    iotargets_foo_bar = {
        'foo':(IOTarget("{foo}_{bar}", suffix=".foo"), None),
        'bar':(IOTarget("{bar}_{foo}", suffix=".bar"), None),
    }
    iotargets_foo_bar_aggregate = {
        'foo':(IOTarget("{foo}_{bar,[^.]+}", suffix=".foo"), IOAggregateTarget("foo_aggregate.txt")),
        'bar':(IOTarget("{bar}_{foo,[^.]+}", suffix=".foo"), IOAggregateTarget("bar_aggregate.txt")),
    }


    def test_init_empty_dict(self):
        with pytest.raises(AssertionError):
            app = Application(name="foo", iotargets=dict())

            
    def test_init(self):
        app = Application(name="foo", iotargets=self.iotargets)


    def test_targets(self):
        app = Application(name="foo", iotargets=self.iotargets_w_suffix, units=self.units)
        assert app.targets == {'foo': ['foo1_bar1.foo', 'foo2_bar2.foo', 'foo3_bar3.foo']}


    def test_foobar_targets(self):
        app = Application(name="foo", iotargets=self.iotargets_foo_bar, units=self.units)
        assert app.targets == {'foo': ['foo1_bar1.foo', 'foo2_bar2.foo', 'foo3_bar3.foo'], 'bar': ['bar1_foo1.bar', 'bar2_foo2.bar', 'bar3_foo3.bar']}


    def test_add_annotation_fn(self):
        app = Application("foo", iotargets=self.iotargets_foo_bar, units=self.units)
        barapp = Application("foo", iotargets=self.iotargets_foo_bar, units=self.units)
                
        assert app._annotation_funcs == {}
        @barapp.register_annotation_fn("foo")
        @app.register_annotation_fn("foo")
        def _annot_func(df, uri, **kwargs):
            return "Added annotation func"

        assert 'foo' in app._annotation_funcs
        assert app._annotation_funcs['foo'](None, None) == "Added annotation func"
        assert barapp._annotation_funcs['foo'](None, None) == "Added annotation func"


    def test_aggregate_targets(self):
        app = Application("foo", iotargets=self.iotargets_foo_bar_aggregate, units=self.units)
        assert app.aggregate_targets == {'bar': 'bar_aggregate.txt', 'foo': 'foo_aggregate.txt'}


    def test_aggregate(self, foo1, foo2, foo3, bar1, bar2, bar3):
        app = Application("foo", iotargets=self.iotargets_foo_bar_aggregate, units=self.units, annotate=True)
        @app.register_annotation_fn("foo")
        def _annot_func(df, uri, iotarget=app.iotargets['foo'], **kwargs):
            m = iotarget[0].search(os.path.basename(uri))
            by = kwargs.get("by", list(iotarget[0].keys()))
            for key in by:
                df[key] = iotarget[0].groupdict[key]
            return df

        # Mock app._targets
        app._targets = {'foo': [str(foo1), str(foo2), str(foo3)], 'bar': [str(bar1), str(bar2), str(bar3)]}
        app.aggregate()
        assert 'foo' in app.aggregate_data['foo'].columns
        assert 'bar' in app.aggregate_data['bar'].columns
        assert set(list(app.aggregate_data['foo']['foo'])) == {'foo1', 'foo2', 'foo3'}
        assert set([os.path.basename(x) for x in list(app.aggregate_data['bar']['uri'])]) == {'bar1_foo1.foo', 'bar2_foo2.foo', 'bar3_foo3.foo'}
