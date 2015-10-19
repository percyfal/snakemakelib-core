# Copyright (C) 2015 by Per Unneberg
"""
SRA sample run organization
-----------------------------
"""
from . import RunRegexp, SampleRegexp, update_config, config, sample_org, join

update_config(
    config, {'settings': {
        'sample_organization' : sample_org(RunRegexp(join("(?P<SM>[a-zA-Z0-9]+)", "(?P<PU>[a-zA-Z0-9]+)", "(?P=PU)")),
                                           RunRegexp(join("(?P<SM>[a-zA-Z0-9]+)", "(?P<PU>[a-zA-Z0-9]+)", "(?P=PU)")),
                                           SampleRegexp(join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")))}})

