# Copyright (C) 2015 by Per Unneberg
import re
from . import resource

COVERAGE_PER_CONTIG_COLUMNS = ["chr", "chrlen", "mapped_bases",
                               "mean_coverage", "sd"]

# resource.register apparently must have a wildcard prefix to work
@resource.register('.*genome_results.txt', priority=20)
def resource_genome_results(uri):
    with open(uri) as fh:
        lines = [re.sub(r'(,|\s+bp.*$|\s+\(.*%\))', r'', x.strip()) for x in fh.readlines() if x.strip() != ""]
    indices = list((i for i, val in enumerate(lines)
                    if val.startswith(">>>"))) + [len(lines)]
    headings = ["_".join(lines[i].split(" ")[1:]) for i in indices[:-1]]
    data = {}
    for i in range(len(indices) - 1):
        ll = lines[(indices[i]+1):indices[i+1]]
        if headings[i] in ["Coverage_per_contig"]:
            data[headings[i]] = [COVERAGE_PER_CONTIG_COLUMNS] + [x.split("\t") for x in ll]
        elif headings[i] in ["Coverage"]:
            pass
        else:
            data[headings[i]] = {y[0]:y[1] for y in [x.split(" = ") for x in ll]}
    return data
