# Copyright (C) 2015 by Per Unneberg
import re
from glob import glob
import pandas as pd
from blaze import resource, DataFrame
from .pandas import annotate_by_uri

@resource.register('.+read_distribution.txt', priority=20)
@annotate_by_uri
def resource_rseqc_read_distribution(uri, **kwargs):
    df = pd.read_table(uri, skiprows=list(range(0,7)) + [18], sep="[ ]+", engine="python")
    df = df.set_index("Group")
    return df


@resource.register('.+geneBody_coverage.geneBodyCoverage.txt', priority=20)
@annotate_by_uri
def resource_rseqc_genebody_coverage(uri, **kwargs):
    df = pd.read_table(uri, header=0)
    return df


@resource.register('.*\*.+', priority=12)
def resource_glob(uri, **kwargs):
    filenames = sorted(glob(uri))
    return pd.concat([resource(f, **kwargs) for f in filenames])
