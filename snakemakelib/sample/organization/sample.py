# Copyright (C) 2015 by Per Unneberg
"""The ``sample`` module defines a generic sample-oriented sample
organization without using platform units. The data is organized in
directories that correspond to samples:

raw_run_re
  ``IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{SM}")``
run_id_re
  ``IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{SM}")``
sample_re
  ``IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{SM}")``

"""
from . import update_config, config, SampleOrganization, join, IOTarget, IOSampleTarget

sample_org = SampleOrganization(IOTarget(join("{SM,[a-zA-Z0-9]+}", "{SM}")),
                                IOTarget(join("{SM,[a-zA-Z0-9]+}", "{SM}")),
                                IOSampleTarget(join("{SM,[a-zA-Z0-9]+}", "{SM}")))

update_config(config, {'settings': {'sample_organization': sample_org}})
