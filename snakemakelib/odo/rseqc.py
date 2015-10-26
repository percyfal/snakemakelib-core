# Copyright (C) 2015 by Per Unneberg
import re
import pandas as pd
from blaze import resource, DataFrame

@resource.register('.+read_distribution.txt', priority=20)
def resource_rseqc_read_distribution(uri):
    df = pd.read_table(uri, skiprows=list(range(0,7)) + [18], sep="[ ]+", engine="python")
    df = df.set_index("Group")
    return df


@resource.register('.+geneBody_coverage.geneBodyCoverage.txt', priority=20)
def resource_rseqc_genebody_coverage(uri):
    df = pd.read_table(uri, header=0)
    return df
