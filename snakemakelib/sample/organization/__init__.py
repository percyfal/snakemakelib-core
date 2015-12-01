# Copyright (C) 2015 by Per Unneberg
from os.path import join
from collections import namedtuple
from snakemake.utils import update_config
try:
    from snakemake.workflow import config
except:
    config = {}
from ..regexp import RunRegexp, SampleRegexp
from ...io import IOTarget, IOSampleTarget

# Define named tuple that holds regular expressions for raw run names,
# run id, and sample identifier
sample_org = namedtuple('sample_organization', 'raw_run_re run_id_re sample_re')

# Add samples configuration string
config['samples'] = config.get("samples", [])
