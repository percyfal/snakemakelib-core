# Copyright (C) 2015 by Per Unneberg
import re
from blaze import resource, DataFrame
import pandas as pd
from .pandas import annotate_by_uri

COVERAGE_PER_CONTIG_COLUMNS = ["chr", "chrlen", "mapped_bases",
                               "mean_coverage", "sd"]


re_trim = re.compile(r'(,|\s+bp.*$|\s+\(.*%\)|%)')

def _split_x(x, delim=" = "):
    y = x.strip().split(delim)
    return [y[0], re_trim.sub("", y[1])]

@resource.register('.*genome_results.txt', priority=20)
@annotate_by_uri
def resource_genome_results(uri, key="Globals", **kwargs):
    with open(uri) as fh:
        data = "".join(fh)
    sections = re.split(">+\s+[a-zA-Z ]+", data)
    section_names = ["Header"] + [re.sub(" ", "_", x) for x in re.findall(">+\s+([a-zA-Z ]+)", data)]
    d = dict()
    for h, sec in zip(section_names, sections):
        if h == "Coverage_per_contig":
            d[h] = DataFrame.from_records([re.split("\s+", x.strip()) for x in sec.split("\n") if x],
                                          columns=COVERAGE_PER_CONTIG_COLUMNS,
                                          index="chr")
            d[h] = d[h].apply(pd.to_numeric)
        elif h in ["Coverage", "Header"]:
            pass
        else:
            d[h] = DataFrame.from_records([_split_x(x) for x in sec.split("\n") if x],
                                          columns=["statistic", "value"],
                                          index="statistic")
            if not h in ["Input"]:
                d[h] = d[h].apply(pd.to_numeric)
    return d[key]
