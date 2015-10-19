# Copyright (C) 2015 by Per Unneberg
"""

"""
from os.path import join
from collections import namedtuple
from snakemake.utils import update_config
from snakemake.workflow import config
from .regexp import RunRegexp, SampleRegexp

# Add samples configuration string
config['samples'] = config.get("samples", [])

# Define named tuple that holds regular expressions for raw run names,
# run id, and sample identifier
sample_org = namedtuple('sample_organization', 'raw_run_re run_id_re sample_re')

