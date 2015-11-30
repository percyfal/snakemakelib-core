# Copyright (C) 2015 by Per Unneberg
import os
import re
from itertools import groupby
import snakemake.workflow
from snakemake.io import _wildcard_regex, regex
from snakemakelib.sample.regexp import RegexpDict
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

class MissingRequiredKeyException(Exception):
    """Exception if required key is missing"""


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


# Based on snakemake.io.regex
def string_format(filepattern):
    f = []
    last = 0
    for match in _wildcard_regex.finditer(filepattern):
        f.append(filepattern[last:match.start()])
        wildcard = match.group("name")
        f.append("{{{}}}".format(wildcard))
        last = match.end()
    f.append(filepattern[last:])
    return "".join(f)



class IOTarget(str):
    """Class for generating and parsing target file names.

    Overrides standard string format function.

    """
    _required_keys = []
    _concat_regex = re.compile("(?P<NAME>[A-Za-z]+)(?P<INDEX>[0-9]+)$")
    _concat = "_"


    def __new__(cls, file, suffix=None):
        obj = str.__new__(cls, file)
        obj._file = file
        obj._regex = None
        obj._format = None
        obj._match = None
        obj._suffix = suffix
        obj._groupdict = dict()
        obj._concat_groupdict = dict()
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
            # compile a regular expression; we remove the $ at end
            pattern = regex(self.file)[:-1]
            self._regex = re.compile(pattern)
        self._groupdict = {k:None for k in self._regex.groupindex.keys()}
        if any([k not in self.keys() for k in self._required_keys]):
            raise MissingRequiredKeyException(
                """some of the required keys {reqkeys} not in regexp {regexp}""".format(
                    reqkeys=",".join(self._required_keys),
                    regexp=self._regex))
        return self._regex


    @property
    def pattern(self):
        return self.regex.pattern
    

    @property
    def basename_pattern(self):
        return os.path.basename(self.pattern)
    

    @property
    def fmt(self):
        if self._format is None:
            # Set the format
            self._format = string_format(self.file)
            if self._suffix:
                self._format += self._suffix
        return self._format


    def _check_format_ok(self, s):
        m = self.regex.search(s)
        if m is None:
            raise Exception("Wrong format for ", s)


    def keys(self):
        return set(self.groupdict.keys())


    def match(self, file, return_instance=False):
        self._match = self.regex.match(file)
        if self._match:
            self._groupdict.update(self._match.groupdict())
        self._concat_indexed_keys()
        if return_instance:
            return self
        return self._match


    def search(self, file, return_instance=False):
        self._match = self.regex.search(file)
        if self._match:
            self._groupdict.update(self._match.groupdict())
        self._concat_indexed_keys()
        if return_instance:
            return self
        return self._match
            

    @property
    def groupdict(self):
        return self._groupdict


    @property
    def concat_groupdict(self):
        return self._concat_groupdict


    def _concat_indexed_keys(self):
        """Concatenate indexed keys"""
        keylist = sorted([(re.sub("[0-9]+$", "", k), k)
                          if re.search("[0-9]+$", k) else (k, k)
                          for k in list(self.groupdict.keys())])
        keymap = {k: [y[1] for y in list(v)]
                  for (k, v) in groupby(keylist, lambda x: x[0])}
        self._concat_groupdict = {
            k: self._concat.join(self.groupdict[mkey] for mkey in group) for k, group in keymap.items()
        }
        self._concat_groupdict.update(self.groupdict)



# Special targets with required key names
class IOSampleTarget(IOTarget):
    _required_keys = ['SM']



class IOAggregateTarget(IOTarget):
    pass
