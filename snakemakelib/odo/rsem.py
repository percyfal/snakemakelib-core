# Copyright (C) 2015 by Per Unneberg
from . import resource, pd

@resource.register('.+\.genes\.results')
def resource_genes_results(uri):
    with open(uri):
        data = pd.read_csv(uri, sep="\t")
    return data

@resource.register('.+\.isoforms\.results')
def resource_isoforms_results(uri):
    with open(uri):
        data = pd.read_csv(uri, sep="\t")
    return data
