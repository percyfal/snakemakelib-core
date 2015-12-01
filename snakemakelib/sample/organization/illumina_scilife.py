# Copyright (C) 2015 by Per Unneberg
"""
sample
-------
"""
from . import RunRegexp, SampleRegexp, update_config, config, sample_org, join, IOTarget, IOSampleTarget


update_config(
    config, {'settings': {
        'sample_organization': sample_org(RunRegexp(join("(?P<SM>P[0-9]+_[0-9]+)", "(?P<DT>[0-9]+)_(?P<PU1>[A-Z0-9]+XX)", "(?P<PU2>[0-9])_(?P=DT)_(?P=PU1)_(?P=SM)")),
                                          RunRegexp(join("(?P<SM>P[0-9]+_[0-9]+)", "(?P<DT>[0-9]+)_(?P<PU1>[A-Z0-9]+XX)", "(?P<PU2>[0-9])_(?P=DT)_(?P=PU1)_(?P=SM)")),
                                          SampleRegexp(join("(?P<SM>P[0-9]+_[0-9]+)", "(?P=SM)")))}})


update_config(
    config, {'settings': {
        'sample_organization': sample_org(IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU1, [A-Z0-9]+XX}", "{PU2, [0-9]}_{DT}_{PU1}_{SM}")),
                                          IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT,[0-9]+}_{PU1,[A-Z0-9]+XX}", "{PU2,[0-9]}_{DT}_{PU1}_{SM}")),
                                          IOSampleTarget(join("{SM,P[0-9]+_[0-9]+}", "{SM}")))}})
