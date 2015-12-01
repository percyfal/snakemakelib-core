# Copyright (C) 2015 by Per Unneberg
"""
SRA sample run organization
-----------------------------
"""
from . import update_config, config, sample_org, join, IOTarget, IOSampleTarget

update_config(
    config, {'settings': {
        'sample_organization': sample_org(IOTarget(join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}", "{PU}")),
                                          IOTarget(join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}", "{PU}")),
                                          IOSampleTarget(join("{SM, [a-zA-Z0-9]+}", "{SM}")))}})

