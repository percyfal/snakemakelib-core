# Copyright (C) 2015 by Per Unneberg
"""Utilities for finding and determining inputs"""
import os
import re
import csv
import pandas as pd
import snakemake.workflow
from snakemake.utils import update_config
from snakemakelib.log import LoggerManager
from snakemakelib.utils import find_files

smllogger = LoggerManager().getLogger(__name__)

def initialize_input(src_re=None, sampleinfo=None, metadata=None,
                     metadata_filter=None, filter_suffix="",
                     sample_column_map=None, sample_filter=None):
    """Initialize inputs.

    Try reading sampleinfo file if present. Returns list of annotated
    dicts.

    Args:
      src_re (IOTarget): IOTarget object corresponding to the source
                           regular expression
      sampleinfo (str): sampleinfo file name
      metadata (str): metadata file name
      metadata (dict): dictionary of filters where the key corresponds
                       to a column and the value the regular expression
                       to match against
      filter_suffix (str): only use given suffix to filter for input
                           file names. Useful if many result files
                           exist for a sample
      sample_column_map (dict): mapping from sampleinfo column names
                                to read group names, e.g.
                                {'Sample':'SM'}
      sample_filter (list): list of sample names to use as subset

    Returns:
      samples (list): list of dicts where each dict corresponds to
                      sample information. The keys are read group
                      identifiers and additional arbitrary metadata
                      information (e.g. factor levels)

    """
    if sampleinfo is None and src_re is None:
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
    if metadata:
        md = pd.read_csv(metadata)
        samples_dict = pd.DataFrame(samples)
        try:
            df = samples_dict.merge(md)
        except:
            raise
        samples = list(df.T.to_dict().values())
        if metadata_filter:
            samples = list(filter(lambda s: all(re.match(v, s[k]) for k,v in metadata_filter.items()), samples))
    if not sample_filter is None:
        samples = [s for s in samples if s["SM"] in sample_filter]

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


def _samples_from_input_files(src_re, filter_suffix="", **kwargs):
    """Generate sample names from input files.

    src_re (IOTarget): IOTarget object corresponding to the source
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
    return [src_re.search(f, return_instance=True).concat_groupdict for f in inputs]
