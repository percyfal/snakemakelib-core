# Copyright (C) 2015 by Per Unneberg
from . import resource, DataFrame

def _hist_reader(uri):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh.readlines()
                if not x.strip() == ""]
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("## METRICS CLASS")
                        or val[0].startswith("## HISTOGRAM")))
        metrics = DataFrame(data[(indices[0]+2):(indices[1])])
        metrics.columns = data[(indices[0]+1)]
        hist = DataFrame(data[(indices[1]+2):])
        hist.columns = data[(indices[1]+1)]
    return (metrics, hist)


def _reader(uri):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh.readlines()
                if not x.strip() == ""]
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("## METRICS CLASS")))
        metrics = DataFrame(data[(indices[0]+2):])
        metrics.columns = data[(indices[0]+1)]
    return metrics
    

@resource.register('.+\.align_metrics')
def resource_align_metrics(uri, **kwargs):
    return _reader(uri)

@resource.register('.+\.insert_metrics')
def resource_insert_metrics(uri, **kwargs):
    return _hist_reader(uri)

@resource.register('.+\.hs_metrics')
def resource_hs_metrics(uri, **kwargs):
    return _hist_reader(uri)

@resource.register('.+\.dup_metrics')
def resource_dup_metrics(uri, **kwargs):
    return _hist_reader(uri)
