# Copyright (C) 2015 by Per Unneberg
from blaze import resource
import pandas as pd

@resource.register('.+\.genes\.results')
def resource_genes_results(uri):
    with open(uri):
        data = pd.read_csv(uri, sep="\t", header=True, comment="#",
                           index_col=["gene_id"])
    return data

@resource.register('.+\.isoforms\.results')
def resource_isoforms_results(uri):
    with open(uri):
        data = pd.read_csv(uri, sep="\t", header=True, comment="#",
                           index_col=["transcript_id"])
    return data
