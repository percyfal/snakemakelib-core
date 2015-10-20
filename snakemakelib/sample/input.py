# Copyright (C) 2015 by Per Unneberg
"""Utilities for finding and determining inputs"""
import os
import csv
import snakemake.workflow
from snakemake.utils import update_config
from snakemakelib.log import LoggerManager
from snakemakelib.utils import find_files

smllogger = LoggerManager().getLogger(__name__)

def initialize_input(src_re=None, sampleinfo=None, filter_suffix="", sample_column_map=None):
    """Initialize inputs.

    Try reading sampleinfo file if present. Returns list of annotated
    dicts.

    Args:
      src_re (RegexpDict): RegexpDict object corresponding to the source
                           regular expression
      sampleinfo (str): sampleinfo file name
      filter_suffix (str): only use given suffix to filter for input
                           file names. Useful if many result files
                           exist for a sample
      sample_column_map (dict): mapping from sampleinfo column names
                                to read group names, e.g.
                                {'Sample':'SM'}

    Returns:
      samples (list): list of dicts where each dict corresponds to
                      sample information. The keys are read group
                      identifiers and additional arbitrary metadata
                      information (e.g. factor levels)

    """
    if not sampleinfo and not src_re:
        raise Exception("must provide either sampleinfo file name or source regular expression")
    if sampleinfo:
        smllogger.info("Reading sample information file ", sampleinfo)
        samples = _parse_sampleinfo(sampleinfo, sample_column_map = sample_column_map)
    else:
        smllogger.info("No sample information file present; trying to set sample information from file names")
        samples = _samples_from_input_files(src_re, filter_suffix = filter_suffix)
    # FIXME: rewrite with try/except
    if not samples:
        raise Exception("No samples parsed")
    return samples

def _parse_sampleinfo(sampleinfo, sample_column_map=None, fmt="csv"):

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
    smllogger.debug("trying to gather target information from configuration key config['settings']['sampleinfo']")
    if isinstance(sampleinfo, str) and not os.path.exists(sampleinfo):
        smllogger.debug("no such sample information file '{sampleinfo}'".format(sampleinfo=sampleinfo))
        return
    smllogger.debug("Reading sample information from '{sampleinfo}'".format(sampleinfo=sampleinfo))
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


def _samples_from_input_files(src_re, filter_suffix=""):
    """Generate sample names from input files.

    src_re (RegexpDict): RegexpDict object corresponding to the source
                         regular expression
    filter_suffix (str): only use given suffix to filter for input
                         file names. Useful if many result files exist
                         for a sample

    Returns:
      samples (list): list of dictionaries, where the keys of each
        dictionary correspond to read group identifiers

    """
    smllogger.debug("Getting sample information from input files")
    inputs = find_files(regexp=src_re.basename_pattern + filter_suffix, **kwargs)
    return [dict(src_re.parse(f)) for f in inputs]
