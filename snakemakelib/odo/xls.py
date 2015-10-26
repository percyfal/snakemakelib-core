# Copyright (C) 2015 by Per Unneberg
import pandas as pd
from blaze import resource
from odo.backends.csv import CSV

@resource.register('.+\.(xls)(.gz)?')
def resource_xls(uri, **kwargs):
    return CSV(uri, **kwargs)
