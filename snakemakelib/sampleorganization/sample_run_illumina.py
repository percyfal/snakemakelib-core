# Copyright (C) 2015 by Per Unneberg
"""
sample_run_illumina
--------------------
"""
import os
from snakemake.utils import update_config
from snakemake.workflow import config
from . import sample_org
from .regexp import RunRegexp, SampleRegexp

config['samples'] = config.get("samples", [])

update_config(
    config, {'settings': {
        'sample_organization': sample_org(RunRegexp(os.path.join("(?P<SM>P[0-9]+_[0-9]+)", "(?P<DT>[0-9]+)_(?P<PU>[A-Z0-9]+XX)", "(?:[0-9])_(?P=DT)_(?P=PU)_(?P=SM)")),
                                          RunRegexp(os.path.join("(?P<SM>P[0-9]+_[0-9]+)", "(?P<DT>[0-9]+)_(?P<PU>[A-Z0-9]+XX)", "(?:[0-9])_(?P=DT)_(?P=PU)_(?P=SM)")),
                                          SampleRegexp(os.path.join("(?P<SM>P[0-9]+_[0-9]+)", "(?P=SM)")))}})
