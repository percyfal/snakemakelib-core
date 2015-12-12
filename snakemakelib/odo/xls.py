# Copyright (C) 2015 by Per Unneberg
import pandas as pd
from blaze import resource

@resource.register('.+\.(xls)(.gz)?')
def resource_xls(uri, **kwargs):
    delimiter = "\t"
    if 'delimiter' in kwargs:
        delimiter = kwargs.pop("delimiter")
    return pd.read_csv(uri, delimiter=delimiter, **kwargs)
