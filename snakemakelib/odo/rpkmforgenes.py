# Copyright (C) 2015 by Per Unneberg
from blaze import resource
import pandas as pd

@resource.register('.+\.rpkmforgenes')
def resource_rpkmforgenes(uri):
    with open(uri):
        data = pd.read_csv(uri, sep="\t", header=None, comment="#",
                           names = ["gene_id", "transcript_id", "FPKM", "TPM"],
                           index_col=["gene_id"])
    return data
