# Copyright (C) 2015 by Per Unneberg
"""Sample organization
===================

The sampleorganization module provides functionality for working with
data organization.

The dictionaries below give examples of some commonly used sample
configurations. A specific sample organization is activated by
setting the 'sample_organization' key below. Configurations must
include:

raw_run_re: RunRegexp for raw data, as delivered from sequencing facility or the like
run_id_re: RunRegexp for run naming, which may or may not be different from 'raw_run_re'
sample_re: SampleRegexp for sample naming

"""
from collections import namedtuple

# Define named tuple that holds regular expressions for raw run names,
# run id, and sample identifier
sample_org = namedtuple('sample_organization', 'raw_run_re run_id_re sample_re')
