# Copyright (C) 2015 by Per Unneberg
"""

"""
from collections import namedtuple

# Define named tuple that holds regular expressions for raw run names,
# run id, and sample identifier
sample_org = namedtuple('sample_organization', 'raw_run_re run_id_re sample_re')
