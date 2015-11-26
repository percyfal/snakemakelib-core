# Copyright (C) 2015 by Per Unneberg
import re
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


    def __new__(cls, file, suffix=None):
        obj = str.__new__(cls, file)
        obj._file = file
        obj._regex = None
        obj._format = None
        obj._match = None
        obj._suffix = suffix
        obj._groupdict = dict()

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
            self._regex = re.compile(regex(self.file)[:-1])
        self._groupdict = {k:None for k in self._regex.groupindex.keys()}
        if any([k not in self.keys() for k in self._required_keys]):
            raise MissingRequiredKeyException(
                """some of the required keys {reqkeys} not in regexp {regexp}""".format(
                    reqkeys=",".join(self._required_keys),
                    regexp=self._regex))
        return self._regex


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


    def match(self, file):
        self._match = self.regex.match(file)
        if self._match:
            self._groupdict.update(self._match.groupdict())
        return self._match


    def search(self, file):
        self._match = self.regex.search(file)
        if self._match:
            self._groupdict.update(self._match.groupdict())
        return self._match
            

    @property
    def groupdict(self):
        return self._groupdict



# Special targets with required key names
class IOSampleTarget(IOTarget):
    _required_keys = ['SM']



class IOAggregateTarget(IOTarget):
    pass
