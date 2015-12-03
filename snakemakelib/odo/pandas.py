# Copyright (C) 2015 by Per Unneberg
import pandas as pd
from blaze import append, DataFrame
from odo.backends import pandas


@append.register(DataFrame, DataFrame)
def append_dataframe_to_dataframe(tgt, src, **kw):
    tgt = pd.concat([tgt, src])
    return tgt


def annotate_by_uri(func):
    def wrap(uri, **kwargs):
        df = func(uri, **kwargs)
        if not kwargs.get('annotate', False):
            return df
        annotation_fn = kwargs.get('annotation_fn', None)
        if not annotation_fn is None:
            df = annotation_fn(df, uri, **kwargs)
        else:
            df['uri'] = uri
        return df
    return wrap
