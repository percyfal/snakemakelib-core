# Copyright (C) 2015 by Per Unneberg
import os
from blaze import DataFrame, odo, resource
import pandas as pd
from snakemakelib.odo.pandas import annotate_by_uri
import pytest


@resource.register('.+\.csv', priority=20)
@annotate_by_uri
def resource_csv_to_df(uri, **kwargs):
    df = pd.read_csv(uri)
    return df


@pytest.fixture(scope="module")
def dataframe1(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('sample1.dataframe1.csv')
    fn.write("""foo,bar\n1,2\n3,4""")
    return fn


@pytest.fixture(scope="module")
def dataframe2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('sample2.dataframe2.csv')
    fn.write("""foo,bar\n5,6\n7,8""")
    return fn


def test_annotate_df(dataframe1, dataframe2):
    df1 = odo(str(dataframe1), DataFrame, annotate=True)
    df2 = df1.append(odo(str(dataframe2), DataFrame, annotate=True))
    assert set([os.path.basename(x) for x in df2['uri']]) == {'sample1.dataframe1.csv', 'sample2.dataframe2.csv'}


def test_custom_annotate_df(dataframe1, dataframe2):
    def _annotate_fn(df, uri, **kwargs):
        uristr = os.path.basename(uri)
        df['sample'] = uristr.split(".")[0]
        return df
    
    df1 = odo(str(dataframe1), DataFrame, annotate=True, annotation_fn=_annotate_fn)
    df2 = df1.append(odo(str(dataframe2), DataFrame, annotate=True, annotation_fn=_annotate_fn))
    assert set(df2['sample']) == {'sample1', 'sample2'}
    
