# Copyright (C) 2015 by Per Unneberg
import re
import string
import math
from datetime import datetime
import pandas as pd
from blaze import odo

# FIXME: utilize pandas builtin functionality for handling these issues
def recast(x, strpfmt="%b %d %H:%M:%S"):
    """Reformat strings to numeric or datestrings"""
    x = x.rstrip().lstrip()
    if re.match('^[0-9]+$', x):
        return int(x)
    elif re.match('^[0-9]+[,\.][0-9]+$', x):
        return float(x.replace(",", "."))
    elif re.search("%", x):
        return float(x.replace(",", ".").replace("%", ""))
    else:
        try:
            dateobj = datetime.strptime(x, strpfmt)
            return dateobj
        except:
            return x


# Replace whitespace with underscore, convert percent characters to PCT
def trim_header(x, underscore=False, percent=False):
    return x.lstrip().rstrip().replace(" ", "_" if underscore else " ").replace("%", "PCT" if percent else "%").replace(",", "_" if underscore else " ")

def annotate_df(infile, parser, groupnames=["SM"]):
    """Annotate a parsed odo unit.
    
    Assumes metadata information is stored in input file name.

    Args:
      infile (str): file name
      parser (re): regexp object to parse input file name with. Metadata information to parse is stored in file name
     
      groupnames (list): list of parser group names to use. For each
      name <name>, the parser should have a corresponding (?P<name>...)
      expression
    """
    df = odo(infile, pd.DataFrame)
    m = parser.parse(infile)
    for name in groupnames:
        df[name] = str(m[name])
    return df
    
