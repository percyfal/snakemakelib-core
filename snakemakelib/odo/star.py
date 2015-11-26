# Copyright (C) 2015 by Per Unneberg
import re
import pandas as pd
from blaze import resource, DataFrame
from .utils import recast
from .pandas import annotate_by_uri

@resource.register('.+\.Log.final.out')
def resource_star_log(uri, annotate=False, **kwargs):
    df = pd.read_table(uri, sep="|",
                       names=["name", "value"],
                       engine="python", skiprows=[7, 22, 27])
    df["name"] = [x.strip() for x in df["name"]]
    df["value"] = [recast(x) for x in df["value"]]
    df = df.set_index("name")
    if annotate:
        df = annotate_by_uri(df, uri, **kwargs)
    return df
