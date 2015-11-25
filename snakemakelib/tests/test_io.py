# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
from os.path import join
import pytest
from ..io import string_format, IOTarget, IOSampleTarget, MissingRequiredKeyException


class TestIOTarget:
    """Test IOTarget class"""
    filepattern = "{key1}_{key2,[0-9]+}"
    f = IOTarget(filepattern)


    def test_wrong_format(self):
        with pytest.raises(Exception):
            self.f.format(**{'key1':'foo', 'key2':'bar'})


    def test_ok_format(self):
        s = self.f.format(**{'key1':'foo', 'key2':234})
        assert s == "foo_234"


    def test_group_dict(self):
        assert self.f.keys() == {'key1', 'key2'}



class TestIOSampleTarget:
    """Test IOSampleTarget class"""
    f = IOSampleTarget(join("{SM, [a-zA-Z0-9]+}", "{SM}.{suffix}"))
    fn = "foo/foo.txt"


    def test_sample_wrong_key(self):
        with pytest.raises(MissingRequiredKeyException):
            IOSampleTarget("{Sample}").regex
        
    
    def test_sample_format(self):
        s = self.f.format(**{'SM': 'foo', 'suffix': 'txt'})
        assert s == "foo/foo.txt"


    def test_sample_parse(self):
        self.f.match(self.fn)
        assert self.f.groupdict == {'suffix': 'txt', 'SM': 'foo'}

