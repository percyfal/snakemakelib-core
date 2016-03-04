# Copyright (C) 2015 by Per Unneberg

from . import update_config, config, SampleOrganization, join, IOTarget, IOSampleTarget

update_config(
    config, {'settings': {
        'sample_organization': SampleOrganization(IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU, [A-Z0-9]+XX}", "{LANE, [0-9]}_{DT}_{PU}_{SM}")),
                                          IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU, [A-Z0-9]+XX}", "{LANE, [0-9]}_{DT}_{PU}_{SM}")),
                                          IOSampleTarget(join("{SM, P[0-9]+_[0-9]+}", "{SM}")))}})

