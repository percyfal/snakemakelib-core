# Copyright (c) 2014 Per Unneberg
import os
import re
from datetime import datetime, date
from snakemakelib.log import LoggerManager
# Circular import issue here!
#
# from snakemakelib.sample.regexp import RegexpDict
# from snakemakelib.sample.regexp import *
import snakemakelib.sample.regexp

smllogger = LoggerManager().getLogger(__name__)


def utc_time():
    """Make an utc_time with appended 'Z'"""
    return str(datetime.utcnow()) + 'Z'


def isoformat(s=None):
    """Return isoformat date from string"""
    if s is None:
        return
    # Assume YYMMDD format
    if len(s) == 6:
        (YY, MM, DD) = (s[0:2], s[2:4], s[4:6])
        return date(int("20{YY}".format(YY=YY)), int(MM.lstrip("0")), int(DD)).isoformat()


def rreplace(string, old, new, occurrence):
    """Replace the last occurrence of an expression in a string.

    See http://stackoverflow.com/questions/2556108/how-to-replace-the-last-occurence-of-an-expression-in-a-string
    """
    li = string.rsplit(old, occurrence)
    return new.join(li)


## From bcbb
def safe_makedir(dname):
    """Make a directory if it doesn't exist, handling concurrent race
    conditions.

    Copied from `bcbio nextgen <https://github.com/chapmanb/bcbio-nextgen>`_

    Args:
      dname (str): directory name
    """
    if not os.path.exists(dname):
        try:
            os.makedirs(dname)
        except OSError:
            if not os.path.isdir(dname):
                raise
    else:
        smllogger.warning("Directory {} already exists; not making directory".format(dname))
    return dname



def find_files(regexp, path=os.curdir, search=False, limit=None, use_full_path=False):
    """Find files in path that comply with a regular expression.

    Args:
      regexp (RegexpDict | str): regular expression object of class
                               <RegexpDict> or <str>
      path (str):   path to search
      search (bool): use re.search instead of re.match for pattern matching
      limit (dict): dictionary where keys correspond to regular expression
             grouping labels and values are lists that limit the
             returned pattern
      use_full_path (bool): use full path in match/search

    Returns:
      flist: list of file names, prepended with root path

    Example:

      The following code block would recursively search for files with
      suffix '.fastq.gz' from the current directory.

      .. code-block:: python

         f = find_files(regex="\w+.fastq.gz")

      By adding the search parameter re.search is used instead of
      re.match. In this case, the following code would find files with
      suffix '.fastq.+':

      .. code-block:: python

         f = find_files(regex="\w+.fastq.gz", search=True)

    """
    if isinstance(regex, IOTarget):
        file_re = regex.re
    else:
        if not regex:
            return []
        file_re = re.compile(regex)
    if not limit is None and any(k not in file_re.groupindex.keys() for k in limit.keys()):
        smllogger.warning("""Some limit keys '{}' not in regex
        groupindex '{}'; disregarding limit option for these
        keys""".format(list(limit.keys()), list(file_re.groupindex.keys())))
    re_fn = file_re.search if search else file_re.match
    flist = []
    for root, dirs, files in os.walk(path):
        for x in files:
            if use_full_path:
                m = re_fn(os.path.join(os.path.normpath(root), x))
            else:
                m = re_fn(x)
            if m is None:
                continue

            if limit:
                if any([m.group(k) in limit[k] for k in limit.keys() if k in m.groupdict().keys()]):
                    flist += [os.path.join(root, x)]
            else:
                flist += [os.path.join(root, x)]
    return sorted(flist)


def dict_to_R(d, as_string=True):
    """Translate a python dictionary to an R option string

    Args:
      d: dictionary

    Returns:
      A string representing an option string of the dictionary in R
    """
    outlist = []
    for (k, v) in d.items():
        if isinstance(v, list):
            if isinstance(v[0], int):
                outlist.append("{k} = c(".format(k=k) + ",".join("{vv}".format(vv=vv) for vv in v) + ")")
            else:
                outlist.append("{k} = c(".format(k=k) + ",".join("'{vv}'".format(vv=vv) for vv in v) + ")")     
        elif isinstance(v, dict):
            outlist.append("{k} = c(".format(k=k) + ",".join("{kk}={vv}".format(kk=kk, vv=vv) for (kk,vv) in v.items()) + ")")
        elif v is True:
            outlist.append("{k}=TRUE".format(k=k))
        elif v is False:
            outlist.append("{k}=FALSE".format(k=k))
        elif v is None:
            outlist.append("{k}=NULL".format(k=k))
        elif isinstance(v, int):
            outlist.append("{k}={v}".format(k=k, v=v))
        elif isinstance(v, float):
            outlist.append("{k}={v}".format(k=k, v=v))
        else:
            outlist.append("{k}='{v}'".format(k=k, v=v))
    return ",".join(outlist)

def dict_to_Rdict(d, as_string=True):
    """Translate a python dictionary to a dict with R-compatible entries

    Args:
      d: dictionary

    Returns:
      A dictionare where values comply with R
    """
    dout = {}
    for (k, v) in d.items():
        if isinstance(v, list):
            if isinstance(v[0], int):
                dout[k] = "c(" + ",".join("{vv}".format(vv=vv) for vv in v) + ")"
            else:
                dout[k] = "c(" + ",".join("'{vv}'".format(vv=vv) for vv in v) + ")"
        elif isinstance(v, dict):
            dout[k] = "c(" + ",".join("{kk}={vv}".format(kk=kk, vv=vv) for (kk,vv) in v.items()) + ")"
        elif v is True:
            dout[k] = "TRUE"
        elif v is False:
            dout[k] = "FALSE"
        elif v is None:
            dout[k] = "NULL"
        elif isinstance(v, int):
            dout[k] = v
        elif isinstance(v, float):
            dout[k] = v
        else:
            dout[k] = '{v}'.format(v=v)
    return dout
