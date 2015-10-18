# Copyright (C) 2015 by Per Unneberg
"""
sample
-------
"""
import os
from snakemake.utils import update_config
from snakemake.workflow import config
from . import sample_org
from .regexp import RunRegexp, SampleRegexp

config['samples'] = config.get("samples", [])

update_config(
    config, {'settings': {
        'sample_organization' :  sample_org(RunRegexp(os.path.join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")),
                                            RunRegexp(os.path.join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")),
                                            SampleRegexp(os.path.join("(?P<SM>[a-zA-Z0-9]+)", "(?P=SM)")))}})
