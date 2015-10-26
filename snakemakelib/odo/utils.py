# Copyright (C) 2015 by Per Unneberg
import re
import string
import math
from datetime import datetime
import pandas as pd

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
