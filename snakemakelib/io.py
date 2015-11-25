# Copyright (C) 2015 by Per Unneberg
import re
import snakemake.workflow
from snakemake.io import _wildcard_regex, regex
from snakemakelib.sample.regexp import RegexpDict
from snakemakelib.log import LoggerManager

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


# From snakemake.io
def string_format(filepattern):
    f = []
    last = 0
    for match in _wildcard_regex.finditer(filepattern):
        f.append(re.escape(filepattern[last:match.start()]))
        wildcard = match.group("name")
        f.append("{{{}}}".format(wildcard))
        last = match.end()
    f.append(re.escape(filepattern[last:]))
    return "".join(f)


class IOTarget(str):
    """Override standard format function"""
    def __new__(cls, file):
        obj = str.__new__(cls, file)
        obj._file = file
        obj._regex = None
        obj._format = None

        return obj


    @property
    def file(self):
        return self._file

    def format(self, **kw):
        s = self.fmt.format(**kw)
        self._check_format_ok(s)
        return s

    @property
    def regex(self):
        if self._regex is None:
            # compile a regular expression
            self._regex = re.compile(regex(self.file))
        return self._regex

    @property
    def fmt(self):
        if self._format is None:
            # Set the format
            self._format = string_format(self.file)
        return self._format
    
    def _check_format_ok(self, s):
        m = self.regex.search(s)
        if m is None:
            raise Exception("Wrong format for ", s)

