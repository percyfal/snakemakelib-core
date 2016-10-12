# Copyright (C) 2015 by Per Unneberg
import os
import re
from itertools import groupby
import snakemake.workflow
from snakemake.io import _wildcard_regex, regex
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

class MissingRequiredKeyException(Exception):
    """Exception if required key is missing"""


def make_targets(tgt_re, samples):
    """Make targets
    
    Create target names based on the target regular expression.

    Args:
      tgt_re (IOTarget): IOTarget object corresponding to the target
                         regular expression

      samples (list): list of dicts where each dict contains labeling information
                      related to a sample. The keys correspond to wildcard group
                      lables.

    Returns:
      targets (list): list of target names

    Example:

      The following code block generates a list of formatted target
      names from a list of sample dictionaries. Here, the dictionary
      keys specify SM and PU wildcard group lables.

      .. code-block:: python

         samples = [{"SM":"foo", "PU":"bar"}, {"SM":"bar", "PU":"foo"}]
         tgt_re = IOTarget("{SM}/{SM}_{PU}.txt")
         tgts = make_targets(tgt_re, samples)
         # tgts is now ['foo/foo_bar.txt', 'bar/bar_foo.txt']

      Note that the same result could be obtained using
      :func:`snakemake.io.expand` and the global :func:`zip` function:

      .. code-block:: python

         from snakemake.io import expand
         tgts = expand("{SM}/{SM}_{PU}.txt", zip, SM=[d["SM"] for d in samples], PU=[d["PU"] for d in samples])

    """
    tgts = list(set(tgt_re.fmt.format(**unit) for unit in samples))
    return tgts


# Based on snakemake.io.regex
def remove_wildcard_restrictions(filepattern):
    """Generate string format without regex restrictions

    Snakemake wildcards are written in the python miniformat language.
    The wildcard regexes can be restricted. For instance, the
    expression {SM, [A-W]+} restricts the wildcard SM to the regex
    [A-W]+. This function returns the wildcards without restrictions.

    The function is a modification of
    :func:`snakemake.io.regex`.

    Args:
      filepattern (str): file pattern expressed as wildcard regexes in python miniformat language

    Returns:
     (str): file pattern without regex restrictions

    Example:

    >>> filepattern = "{key1}_{key2,[0-9]+}"
    >>> remove_wildcard_restrictions(filepattern)
    '{key1}_{key2}'

    """
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

    The class is modelled on :class:`snakemake.io._IOFile`.

    Example:

    >>> from snakemakelib.io import IOTarget
    >>> import os
    >>> f = IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}"))
    >>> f.regex
    re.compile(r'(?P<SM>[a-zA-Z0-9]+)\/(?P<PU>[a-zA-Z0-9]+)', re.UNICODE)
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
        """Return file name; basically the string that self refers to"""
        return self._file


    def format(self, **kw):
        """Format self according to keyword arguments.

        Checks that format is ok.

        Example:

        >>> f = IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{SM}.{suffix}"))
        >>> s = f.format(**{'SM':'foo', 'suffix': 'txt'})
        >>> print(s)
        'foo/foo.txt'
        >>>  # The following throws an error due to disallowed _ character
        >>> s = f.format(**{'SM':'foo_bar', 'suffix': 'txt'})
        Exception: ('Wrong format for ', 'foo_bar/foo_bar.txt')
        """
        s = self.fmt.format(**kw)
        self._check_format_ok(s)
        return s


    @property
    def regex(self):
        """Compile a regular expression of self.file.

        Utilizes :func:`snakemake.io.regex` which adds "$" to the
        pattern. Since `IOTarget` allows suffixes, $ is stripped from
        the regex.

        The groupindex keys are stored in self._groupdict for easy
        access.

        Returns:
          :py:mod:`re`: Compiled regular expression.
        """
        if self._regex is None:
            # compile a regular expression; we remove the $ at end
            pattern = regex(self.file)[:-1]
            self._regex = re.compile(pattern)
        self._groupdict = {k:None for k in self._regex.groupindex.keys()}
        if any([k not in self.keys() for k in self._required_keys]):
            raise MissingRequiredKeyException(
                """some of the required keys {reqkeys} not in regex {regex}""".format(
                    reqkeys=",".join(self._required_keys),
                    regex=self._regex))
        return self._regex


    @property
    def pattern(self):
        """Get the regex pattern."""
        return self.regex.pattern
    

    @property
    def basename_pattern(self):
        """Get the basename pattern, excluding path"""
        return os.path.basename(self.pattern)
    

    @property
    def fmt(self):
        """Return the format for string formatting"""
        if self._format is None:
            # Set the format
            self._format = remove_wildcard_restrictions(self.file)
            if self._suffix:
                self._format += self._suffix
        return self._format


    def _check_format_ok(self, s):
        """Make sure the format complies to the regex"""
        m = self.regex.search(s)
        if m is None:
            raise Exception("Wrong format for ", s)


    def keys(self):
        """Get the regex groupdict keys"""
        return set(self.groupdict.keys())


    def match(self, file, return_instance=False):
        """Match file to regex.

        Args:
          file (str): file name to match against
          return_instance (bool): return self

        Returns:
          (re): match object


        Example:

          .. code-block:: python

             >>> s = "GSM123456/SRR123456_1.fastq.gz"
             >>> f = IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}"))
             >>> f.match(s)
             >>> print(f.groupdict)
             {'PU': 'SRR123456', 'SM': 'GSM123456'}
        """
        self._match = self.regex.match(file)
        if self._match:
            self._groupdict.update(self._match.groupdict())
        self._concat_indexed_keys()
        if return_instance:
            return self
        return self._match


    def search(self, file, return_instance=False):
        """Search file with regex.

        Args:
          file (str): file name to search
          return_instance (bool): return self

        Returns:
          (re): match object

        Example:

          .. code-block:: python

             >>> s = "GSM123456/SRR123456_1.fastq.gz"
             >>> f = IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}"))
             >>> f.search(s)
             >>> print(f.groupdict)
             {'PU': 'SRR123456', 'SM': 'GSM123456'}

        """
        self._match = self.regex.search(file)
        if self._match:
            self._groupdict.update(self._match.groupdict())
        self._concat_indexed_keys()
        if return_instance:
            return self
        return self._match
            

    # NB: for consistency with the re module, this should be a function
    @property
    def groupdict(self):
        """Get the groupdict.        """
        return self._groupdict


    @property
    def concat_groupdict(self):
        """Get the concatenated groupdict.

        It is possible to index wildcard groups, e.g. SM1, SM2, ...
        The concat_groupdict contains concatenated versions of indexed
        groups so that SM would return the concatenated version of the
        values of SM1, SM2, ...

        """
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



# TODO: update class for use case - use mixin class?
class IOReadGroup(dict):
    """Container class for read group information.

        The labels are named following the conventions of the
    `SAM format specification <http://samtools.github.io/hts-specs/SAMv1.pdf>`_.
    To summarize, the class provides the following keys:

    RG
      Read group. Unordered multiple @RG lines are allowed.
    ID*
      Read group identifer. Each @RG line must have a unique ID. The
      value of ID is used in the RG tags of alignment records. Must be
      unique among all read groups in header section. Read group IDs may
      be modified when merging SAMfiles in order to handle collisions.
    CN
      Name of sequencing center producing the read.
    DS
      Description.
    DT
      Date the run was produced (ISO8601 date or date/time).

    FO
      Flow order. The array of nucleotide bases that correspond to
      the nucleotides used for each ow of each read. Multi-base rows are
      encoded in IUPAC format, and non-nucleotide rows by various other
      characters. Format: /\*|[ACMGRSVTWYHKDBN]+/
    KS
      The array of nucleotide bases that correspond to the key
      sequence of each read.
    LB
      Library.
    PG
      Programs used for processing the read group.
    PI
      Predicted median insert size.
    PL
      Platform/technology used to produce the reads. Valid values:
      CAPILLARY, LS454, ILLUMINA, SOLID, HELICOS, IONTORRENT, ONT, and
      PACBIO.
    PM
      Platform model. Free-form text providing further details of the
      platform/technology used.
    PU
      Platform unit (e.g. flowcell-barcode.lane for Illumina or slide
      for SOLiD). Unique identifier.
    SM
      Sample. Use pool name where a pool is being sequenced.

    """
    _group_keys = ['ID', 'CN', 'DS', 'DT', 'FO', 'KS',
                   'LB', 'PG', 'PI', 'PL', 'PU', 'SM']
    _group_dict = {'ID': 'identifier', 'CN': 'center', 'DS': 'description',
                   'DT': 'date', 'FO': 'floworder', 'KS': 'keysequence',
                   'LB': 'library', 'PG': 'program', 'PI': 'insertsize',
                   'PL': 'platform', 'PU': 'platform-unit', 'SM': 'sample'}


    def __init__(self, iotarget=None, opt_prefix="--", *args, **kwargs):
        if not iotarget is None:
            super(IOReadGroup, self).__init__(iotarget, *args, **kwargs)
        self._opt_prefix = opt_prefix
        self._iotarget = iotarget
        if 'ID' not in self.keys() or not self.get('ID', ""):
            # inv_map = {v: k for (k, v) in list(self.re.groupindex.items())}
            try:
                self['ID'] = os.path.basename(self._iotarget.fmt.format(**self._iotarget))
            except:
                self['ID'] = "unknown"


    def _fmt_string(self, k):
        """Take care of date string"""
        if k == 'DT':
            return snakemakelib.utils.isoformat(self[k])
        return self[k]


    def __str__(self):
        """Return a generic program string"""
        return " ".join([
            "{dash}{key} {value}".format(dash=self._opt_prefix,
                                         key=self._group_dict[k],
                                         value=self._fmt_string(k))
            for k in sorted(list(self.keys())) if not self[k] is None
            and k in self._group_keys])
