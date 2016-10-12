# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
from os.path import join
import pandas as pd
from snakemakelib.odo.pandas import annotate_by_uri
from blaze import DataFrame, odo, resource
import pytest
from snakemakelib.io import make_targets, remove_wildcard_restrictions, IOTarget, IOSampleTarget, MissingRequiredKeyException, IOReadGroup


@resource.register('.+\.csv', priority=20)
@annotate_by_uri
def resource_csv_to_df(uri, **kwargs):
    df = pd.read_csv(uri)
    return df


@pytest.fixture(scope="module")
def dataframe1(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo_123_1.csv')
    fn.write("""foo,bar\n1,2\n3,4""")
    return fn


@pytest.fixture(scope="module")
def dataframe2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('foo_456_1.csv')
    fn.write("""foo,bar\n5,6\n7,8""")
    return fn


def test_make_targets():
    samples = [{"SM":"foo", "PU":"bar"}, {"SM":"bar", "PU":"foo"}]
    tgt_re = IOTarget("{SM}/{SM}_{PU}.txt")
    tgts = make_targets(tgt_re, samples)
    assert "foo/foo_bar.txt" in tgts


def test_remove_wildcard_restrictions():
    filepattern = "{key1}_{key2,[0-9]+}"
    f = remove_wildcard_restrictions(filepattern)
    assert f == "{key1}_{key2}"



class TestIOTarget:
    """Test IOTarget class"""
    filepattern = "{key1}_{key2,[0-9]+}"
    f = IOTarget(filepattern)
    f2 = IOTarget(filepattern, suffix=".suffix")
    f3 = IOTarget(join("{key1}", filepattern))
    filename = "foo_123.suffix"
    filename_short = "foo_123"


    def test_iotarget_init_empty(self):
        with pytest.raises(TypeError):
            IOTarget()


    def test_wrong_format(self):
        with pytest.raises(Exception):
            self.f.format(**{'key1':'foo', 'key2':'bar'})


    def test_ok_format(self):
        s = self.f.format(**{'key1':'foo', 'key2':234})
        assert s == "foo_234"


    def test_group_dict(self):
        assert self.f.keys() == {'key1', 'key2'}


    def test_target_w_suffix(self):
        """Test matching to filename with and without suffix"""
        self.f2.match(self.filename)
        assert self.f2.groupdict == {'key1': 'foo', 'key2': '123'}
        self.f2.search(self.filename_short)
        assert self.f2.groupdict == {'key1': 'foo', 'key2': '123'}
        s = self.f2.format(**{'key1':'foo', 'key2':123})
        assert s == "foo_123.suffix"

        
    def test_concat_keys(self):
        tgt = IOTarget("{key2}_{key1}_{foo,[^\.]+}", suffix=".txt")
        tgt.match("KEY2_KEY1_FOO.txt")
        assert tgt.concat_groupdict == {'foo': 'FOO', 'key': 'KEY1_KEY2', 'key1': 'KEY1', 'key2': 'KEY2'}


    def test_regex(self):
        """Test format of compiled regex expression"""
        tgt = IOTarget("{key2}_{key1}_{foo,[^\.]+}", suffix=".txt")
        assert 're.compile(\'(?P<key2>.+)_(?P<key1>.+)_(?P<foo>[^\\\\.]+)\')' == str(tgt.regex)

        
    def test_basename_pattern(self):
        """Test the basename pattern for regex with path separator"""
        assert "(?P<key1>.+)\/(?P=key1)_(?P<key2>[0-9]+)" == self.f3.pattern
        assert "(?P=key1)_(?P<key2>[0-9]+)" == self.f3.basename_pattern


    def test_basename_pattern_wo_path(self):
        """Test the basename pattern for regex without path separator"""
        assert "(?P<key1>.+)_(?P<key2>[0-9]+)" == self.f2.pattern
        assert "(?P<key1>.+)_(?P<key2>[0-9]+)" == self.f2.basename_pattern



class TestIOSampleTarget:
    """Test IOSampleTarget class"""
    f = IOSampleTarget(join("{SM, [a-zA-Z0-9]+}", "{SM}.{suffix}"))
    filename = "foo/foo.txt"


    def test_sample_missing_required_key(self):
        """IOSampleTarget requires key SM"""
        with pytest.raises(MissingRequiredKeyException):
            IOSampleTarget("{Sample}").regex


    def test_sample_wrong_indexed_key(self):
        IOSampleTarget("{SM,[0-9]+}_{ID1,[0-9+]}")


    def test_sample_format(self):
        s = self.f.format(**{'SM': 'foo', 'suffix': 'txt'})
        assert s == "foo/foo.txt"


    def test_sample_parse(self):
        self.f.match(self.filename)
        assert self.f.groupdict == {'suffix': 'txt', 'SM': 'foo'}


# FIXME
class TestIOReadGroup:
    """Test IOReadGroup class"""


    def test_read_group_init(self):
        s = IOReadGroup()
        print(dir(s))
        print(s.keys())
        print(s)
