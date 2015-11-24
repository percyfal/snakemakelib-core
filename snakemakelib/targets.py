# Copyright (C) 2015 by Per Unneberg
import re
import os
import csv
import snakemake.workflow
from snakemakelib.sample.regexp import RegexpDict
from snakemakelib.utils import find_files
from snakemakelib.log import LoggerManager
from snakemakelib.exceptions import DeprecatedException

smllogger = LoggerManager().getLogger(__name__)

def make_targets(tgt_re, samples, target_suffix=""):
    """Make targets
    
    Create target names based on the target regular expression and a
    target suffix.

    Args:
      tgt_re (RegexpDict): RegexpDict object corresponding to the target
                           regular expression

      samples (list): list of dicts where each dict is an annotated
                      sample. The keys correspond to read group labels.
      target_suffix (str): target suffix to add to target regexp

    Returns:
      targets (list): list of target names
    """
    tgts = list(set(tgt_re.fmt.format(**unit) + target_suffix for unit in samples))
    return tgts
