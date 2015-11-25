# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
import pytest
from ..io import string_format, IOTarget

filepattern = "{key1}_{key2,[0-9]+}"
f = IOTarget(filepattern)

class TestIOTarget:
    """Test IOTarget class"""

    def test_wrong_format(self):
        with pytest.raises(Exception):
            f.format(**{'key1':'foo', 'key2':'bar'})

    def test_ok_format(self):
        f.format(**{'key1':'foo', 'key2':234})

    
