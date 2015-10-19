# Copyright (C) 2015 by Per Unneberg
"""Utilities for finding and determining inputs"""
import os
import csv
from snakemakelib.log import LoggerManager
from snakemakelib.utils import find_files

logger = LoggerManager().getLogger(__name__)


def parse_sampleinfo(sampleinfo, sample_column_map=None, fmt="csv"):
    """Parse sample information file

    Args:
      sampleinfo (str): sampleinfo file name. Each line in the file
        should correspond to one input unit, where columns represent
        read group identifiers used be the sample organization regular
        expressions.
      sample_column_map (dict): mapping from sampleinfo column names to
                         regexp group names, e.g.
                         {'SampleID':'SM', 'Lane':'PU1'}
      fmt (str): input file format

    Returns:
      samples (list): list of dictionaries, where the keys of each
        dictionary correspond to read group identifiers
    """
    logger.debug("trying to gather target information from configuration key config['settings']['sampleinfo']")
    if isinstance(sampleinfo, str) and not os.path.exists(sampleinfo):
        logger.debug("no such sample information file '{sampleinfo}'".format(sampleinfo=sampleinfo))
        return
    logger.debug("Reading sample information from '{sampleinfo}'".format(sampleinfo=sampleinfo))
    if isinstance(sampleinfo, str):
        with open(sampleinfo, 'r') as fh:
            reader = csv.DictReader(fh.readlines())
    else:
        reader = sampleinfo
        assert type(reader) is csv.DictReader,\
            "sampleinfo is not a 'csv.DictReader'; " +\
        "if not a file name, must be a 'csv.DictReader'"
    if sample_column_map:
        reader.fieldnames = [sample_column_map.get(fn, fn) for fn in reader.fieldnames]
    return [s for s in reader]


def samples_from_input_files(src_re, filter_suffix="", **kwargs):
    """Generate sample names from input files.

    """
    logger.debug("Getting sample information from input files")
    inputs = find_files(regexp=src_re.basename_pattern + filter_suffix, **kwargs)
    return [dict(src_re.parse(f)) for f in inputs]
