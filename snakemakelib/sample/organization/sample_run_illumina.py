# Copyright (C) 2015 by Per Unneberg
"""
sample_run_illumina
--------------------
"""
from . import update_config, config, sample_org, join, IOTarget, IOSampleTarget

update_config(
    config, {'settings': {
        'sample_organization': sample_org(IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU, [A-Z0-9]+XX}", "{LANE, [0-9]}_{DT}_{PU}_{SM}")),
                                          IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU, [A-Z0-9]+XX}", "{LANE, [0-9]}_{DT}_{PU}_{SM}")),
                                          IOSampleTarget(join("{SM, P[0-9]+_[0-9]+}", "{SM}")))}})

