# Copyright (C) 2015 by Per Unneberg
"""
sample
-------
"""
from . import RunRegexp, SampleRegexp, update_config, config, sample_org, join

update_config(
    config, {'settings': {
        'sample_organization' :  sample_org(RunRegexp(join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")),
                                            RunRegexp(join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")),
                                            SampleRegexp(join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")))}})
