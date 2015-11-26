# Copyright (C) 2015 by Per Unneberg
import pandas as pd
from blaze import append, DataFrame
from odo.backends import pandas


@append.register(DataFrame, DataFrame)
def append_dataframe_to_dataframe(tgt, src, **kw):
    tgt = pd.concat([tgt, src])
    return tgt


def annotate_by_uri(df, uri, **kwargs):
    if not kwargs.get('annotation_fn') is None:
        func = kwargs.pop('annotation_fn')
        return func(df, uri, **kwargs)
    else:
        df['uri'] = uri
    return df
