# Copyright (C) 2015 by Per Unneberg
"""Provide :class:`SampleOrganization` objects with  predefined
:class:`~snakemakelib.io.IOTarget` objects that define what input and
output file prefixes should look like at given levels of organization.

A specific sample organization is activated by importing a submodule
from :mod:`snakemakelib.sample.organization` that reflects the file
naming conventions. Upon loading, the ``sample_organization`` key is
updated and set to a :class:`SampleOrganization` instance.
"""
from os.path import join
from snakemake.utils import update_config
try:
    from snakemake.workflow import config
except:
    global config
    config = dict()
from ...io import IOTarget, IOSampleTarget
from .utils import SampleOrganization


# Add samples configuration string
config['samples'] = config.get("samples", [])
