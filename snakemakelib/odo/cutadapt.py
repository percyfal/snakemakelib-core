# Copyright (C) 2015 by Per Unneberg
import re
from . import resource, convert, DataFrame

class Cutadapt(object):
    def __init__(self, path, **kwargs):
        self.path = path

@resource.register('.+\.cutadapt_metrics')
def resource_cutadapt_metrics(uri, **kwargs):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh.readlines()
                if not x.strip() == ""]
        # Find indices of "===" lines that separate the sections
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("===")))
        # Only read the first tabes
        summary = (list([
            re.sub(r'([ ]?\(\d+\.\d+%\)|,|[ ]?bp| $)', r'', z.strip(" "))
            for z in x
        ]
                        for x in list(y.split(":")
                                      for x in data[indices[0]+1:indices[1]]
                                      for y in x)))
        df = DataFrame(summary)
        df.columns = ["statistic", "value"]
    return df


# @convert.register(DataFrame, Cutadapt)
# def cutadapt_to_DataFrame(cutadapt):
#     pass
    
