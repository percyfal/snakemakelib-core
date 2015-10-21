# Copyright (C) 2015 by Per Unneberg
from . import resource, pd

def _hist_reader(uri):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh.readlines()
                if not x.strip() == ""]
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("## METRICS CLASS")
                        or val[0].startswith("## HISTOGRAM")))
    return [data[(indices[0]+1):(indices[1])], data[(indices[1]+1):]]


def _reader(uri):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh.readlines()
                if not x.strip() == ""]
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("## METRICS CLASS")))
    return data[(indices[0]+1):]
    

@resource.register('.+\.align_metrics')
def resource_align_metrics(uri):
    return _reader(uri)

@resource.register('.+\.insert_metrics')
def resource_insert_metrics(uri):
    return _hist_reader(uri)

@resource.register('.+\.hs_metrics')
def resource_hs_metrics(uri):
    return _hist_reader(uri)

@resource.register('.+\.dup_metrics')
def resource_dup_metrics(uri):
    return _hist_reader(uri)
