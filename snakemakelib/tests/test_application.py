# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
import os
import logging
import pytest
import pandas as pd
from blaze import DataFrame, resource
from ..application import Application, PlatformUnitApplication, SampleApplication
from ..io import IOTarget, IOSampleTarget, IOAggregateTarget
logging.basicConfig(level=logging.DEBUG)
from snakemakelib.odo import pandas

@resource.register('.+\.foo')
@pandas.annotate_by_uri
def resource_foo_to_df(uri, **kwargs):
    df = pd.read_csv(uri)
    return df


@pytest.fixture(scope="module")
def foo1(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo1_bar1.foo')
    fn.write("""foo,bar\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def foo2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo2_bar2.foo')
    fn.write("""foo,bar\n5,6\n7,8""")
    return fn

@pytest.fixture(scope="module")
def foo3(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo3_bar3.foo')
    fn.write("""foo,bar\n9,10\n11,12""")
    return fn

@pytest.fixture(scope="module")
def bar1(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('bar1_foo1.foo')
    fn.write("""bar,foo\n1,2\n3,4""")
    return fn

@pytest.fixture(scope="module")
def bar2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('bar2_foo2.foo')
    fn.write("""bar,foo\n5,6\n7,8""")
    return fn

@pytest.fixture(scope="module")
def bar3(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('bar3_foo3.foo')
    fn.write("""bar,foo\n9,10\n11,12""")
    return fn


@pytest.fixture(scope="module")
def units():
    return [
        {'foo': 'foo1', 'bar': 'bar1'},
        {'foo': 'foo2', 'bar': 'bar2'},
        {'foo': 'foo3', 'bar': 'bar3'}
    ]



class TestApplication:
    """Test application class"""
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


    def test_targets(self, units):
        app = Application(name="foo", iotargets=self.iotargets_w_suffix, units=units)
        assert app.targets == {'foo': ['foo1_bar1.foo', 'foo2_bar2.foo', 'foo3_bar3.foo']}


    def test_targets_no_run(self, units):
        app = Application(name="foo", iotargets=self.iotargets_w_suffix, units=units, run=False)
        assert app.targets == {'foo': []}

        
    def test_foobar_targets(self, units):
        app = Application(name="foo", iotargets=self.iotargets_foo_bar, units=units)
        assert app.targets == {'foo': ['foo1_bar1.foo', 'foo2_bar2.foo', 'foo3_bar3.foo'], 'bar': ['bar1_foo1.bar', 'bar2_foo2.bar', 'bar3_foo3.bar']}


    def test_add_annotation_fn(self, units):
        app = Application("foo", iotargets=self.iotargets_foo_bar, units=units)
        barapp = Application("foo", iotargets=self.iotargets_foo_bar, units=units)
                
        assert app._annotation_funcs == {}
        @barapp.register_annotation_fn("foo")
        @app.register_annotation_fn("foo")
        def _annot_func(df, uri, **kwargs):
            return "Added annotation func"

        assert 'foo' in app._annotation_funcs
        assert app._annotation_funcs['foo'](None, None) == "Added annotation func"
        assert barapp._annotation_funcs['foo'](None, None) == "Added annotation func"


    def test_aggregate_targets(self, units):
        app = Application("foo", iotargets=self.iotargets_foo_bar_aggregate, units=units)
        assert app.aggregate_targets == {'bar': 'bar_aggregate.txt', 'foo': 'foo_aggregate.txt'}


    def test_aggregate(self, foo1, foo2, foo3, bar1, bar2, bar3, units):
        app = Application("foo", iotargets=self.iotargets_foo_bar_aggregate, units=units, annotate=True)
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


        
@pytest.fixture(scope="module")
def SM_PU_iotargets_foo_bar_aggregate():
    return {
        'foo':(IOTarget("{PATH}/{SM}_{PU,[^.]+}", suffix=".foo"), IOAggregateTarget("foo_aggregate.txt")),
        'bar':(IOTarget("{PATH}/{SM}_{PU,[^.]+}", suffix=".foo"), IOAggregateTarget("bar_aggregate.txt")),
    }



class TestPlatformUnitApplication:
    """Test PlatformUnitApplication class"""


    def test_aggregate(self, foo1, foo2, foo3, bar1, bar2, bar3, SM_PU_iotargets_foo_bar_aggregate, units):
        app = PlatformUnitApplication(name="foo", iotargets=SM_PU_iotargets_foo_bar_aggregate, units=units)
        app._targets = {'foo': [str(foo1), str(foo2), str(foo3)], 'bar': [str(bar1), str(bar2), str(bar3)]}
        app.aggregate()
        assert list(app.aggregate_data['foo']['PU']) == ['bar1', 'bar1', 'bar2', 'bar2', 'bar3', 'bar3']
        assert list(app.aggregate_data['foo']['SM']) == ['foo1', 'foo1', 'foo2', 'foo2', 'foo3', 'foo3']
        assert list(app.aggregate_data['foo']['PlatformUnit']) == ['foo1__bar1', 'foo1__bar1', 'foo2__bar2', 'foo2__bar2', 'foo3__bar3', 'foo3__bar3']

        

class TestSampleApplication:
    """Test SampleApplication class"""


    def test_aggregate(self, foo1, foo2, foo3, bar1, bar2, bar3, SM_PU_iotargets_foo_bar_aggregate, units):
        app = SampleApplication(name="foo", iotargets=SM_PU_iotargets_foo_bar_aggregate, units=units)
        app._targets = {'foo': [str(foo1), str(foo2), str(foo3)], 'bar': [str(bar1), str(bar2), str(bar3)]}
        app.aggregate()
        assert list(app.aggregate_data['foo']['SM']) == ['foo1', 'foo1', 'foo2', 'foo2', 'foo3', 'foo3']

