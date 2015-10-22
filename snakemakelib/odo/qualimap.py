# Copyright (C) 2015 by Per Unneberg
import re
from . import resource, DataFrame

COVERAGE_PER_CONTIG_COLUMNS = ["chr", "chrlen", "mapped_bases",
                               "mean_coverage", "sd"]

# resource.register apparently must have a wildcard prefix to work
# Set priority to override default text resources
@resource.register('.*genome_results.txt', priority=20)
def resource_genome_results(uri, **kwargs):
    with open(uri) as fh:
        lines = [re.sub(r'(,|\s+bp.*$|\s+\(.*%\))', r'', x.strip()) for x in fh.readlines() if x.strip() != ""]
    indices = list((i for i, val in enumerate(lines)
                    if val.startswith(">>>"))) + [len(lines)]
    headings = ["_".join(lines[i].split(" ")[1:]) for i in indices[:-1]]
    data = {}
    for i in range(len(indices) - 1):
        ll = lines[(indices[i]+1):indices[i+1]]
        if headings[i] in ["Coverage_per_contig"]:
            data[headings[i]] =  DataFrame([x.split("\t") for x in ll])
            data[headings[i]].columns = [COVERAGE_PER_CONTIG_COLUMNS]
        elif headings[i] in ["Coverage"]:
            pass
        else:
            data[headings[i]] = DataFrame([x.split(" = ") for x in ll])
            data[headings[i]].columns = ['statistic', 'value']
    return data
