# Copyright (C) 2015 by Per Unneberg
import re
from blaze import resource, DataFrame
import numpy as np
import pandas as pd
from .pandas import annotate_by_uri

# Potentially add regexp for adapter sections as these are repetitive
adapter_re = re.compile(r'''
===\s*(?P<Read>(First read|Second read)?):?\s+Adapter\s+'(?P<Adapter>[^\s]+)'\s+===
'''    
)

re_trim = re.compile(r'(\([0-9.]+%\)|,| |bp)')

def _split_x(x, delim=":"):
    y = x.strip().split(delim)
    return [y[0], re_trim.sub("", y[1])]

# For now only return the summary section
@resource.register('.+\.cutadapt_metrics')
@annotate_by_uri
def resource_cutadapt_metrics(uri, **kwargs):
    with open(uri) as fh:
        data = "".join(fh)
    sections = re.split("\n===.*===\n", data)
    df = DataFrame.from_records([_split_x(x) for x in sections[1].split("\n") if x],
                                index=["statistic"], columns=["statistic", "value"])
    df["value"] = pd.to_numeric(df["value"])
    return df

