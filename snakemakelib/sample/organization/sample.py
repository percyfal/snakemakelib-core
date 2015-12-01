# Copyright (C) 2015 by Per Unneberg
"""
sample
-------
"""
from . import update_config, config, sample_org, join, IOTarget, IOSampleTarget

update_config(
    config, {'settings': {
        'sample_organization': sample_org(IOTarget(join("{SM, [a-zA-Z0-9]+}", "{SM}")),
                                          IOTarget(join("{SM, [a-zA-Z0-9]+}", "{SM}")),
                                          IOSampleTarget(join("{SM,[a-zA-Z0-9]+}", "{SM}")))}})
