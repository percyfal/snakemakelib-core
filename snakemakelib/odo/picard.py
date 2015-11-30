# Copyright (C) 2015 by Per Unneberg
from blaze import resource, DataFrame
import pandas as pd
import re
from .pandas import annotate_by_uri


def _hist_reader(uri):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh
                if not x.strip() == ""]
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("## METRICS CLASS")
                        or val[0].startswith("## HISTOGRAM")))
        metrics = DataFrame.from_records(data[(indices[0]+2):(indices[1])],
                                         columns=data[(indices[0]+1)])

        hist = DataFrame.from_records(data[(indices[1]+2):],
                                      columns = data[(indices[1]+1)])
    return (metrics, hist)


def _reader(uri):
    with open(uri) as fh:
        data = [x.strip("\n").split("\t") for x in fh
                if not x.strip() == ""]
        indices = list((i for i, val in enumerate(data)
                        if val[0].startswith("## METRICS CLASS")))
        metrics = DataFrame.from_records(data[(indices[0]+2):],
                                         columns=data[(indices[0]+1)],
                                         index="CATEGORY")
    return (metrics, None)
    

@resource.register('.+\.align_metrics')
@annotate_by_uri
def resource_align_metrics(uri, **kwargs):
    metrics, _ = _reader(uri)
    metrics = metrics.apply(pd.to_numeric, axis=1)
    return metrics

@resource.register('.+\.insert_metrics')
@annotate_by_uri
def resource_insert_metrics(uri, key="insert_metrics", **kwargs):
    (_metrics, hist) = _hist_reader(uri)
    metrics = _metrics[_metrics.columns.difference(["PAIR_ORIENTATION"])].apply(pd.to_numeric, axis=0)
    metrics["PAIR_ORIENTATION"] = _metrics["PAIR_ORIENTATION"]
    hist = hist.apply(pd.to_numeric, axis=0)
    if key == "insert_metrics":
        return metrics
    elif key == "insert_metrics_hist":
        return hist

@resource.register('.+\.hs_metrics')
@annotate_by_uri
def resource_hs_metrics(uri, **kwargs):
    return _hist_reader(uri)


@resource.register('.+\.dup_metrics')
@annotate_by_uri
def resource_dup_metrics(uri, key="dup_metrics", **kwargs):
    (_metrics, hist) = _hist_reader(uri)
    metrics = _metrics[_metrics.columns.difference(["LIBRARY"])].apply(pd.to_numeric, axis=0)
    hist = hist.apply(pd.to_numeric, axis=0)
    if key == "dup_metrics":
        return metrics
    elif key == "dup_metrics_hist":
        return hist

