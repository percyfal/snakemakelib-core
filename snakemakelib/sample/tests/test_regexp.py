# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103
import re
import os
import pytest
from itertools import groupby
from snakemakelib.sample.regexp import RegexpDict, SampleRegexp, ReadGroup, DisallowedKeyException, MissingRequiredKeyException

class TestRegexpDict:
    def test_regexpdict_init_empty(self):
        with pytest.raises(TypeError):
            rd = RegexpDict()

    def test_regexpdict_init_wrong_keys(self):
        with pytest.raises(DisallowedKeyException):
            rd = RegexpDict("(?P<PU1>[A-Z0-9]+)_(?P<PU2>[0-9]+)")

    def test_regexpdict_basename_pattern(self):
        rd = SampleRegexp(os.path.join("(?P<SM>[a-z]+)", "(?P<PU>[0-9]+)_(?P=SM)"))
        assert rd.pattern == "(?P<SM>[a-z]+)/(?P<PU>[0-9]+)_(?P=SM)"
        assert rd.basename_pattern == "(?P<PU>[0-9]+)_(?P<SM>[a-z]+)"

    def test_regexpdict_relative_basename_pattern(self):
        """Test basename of sample regexp without leading paths"""
        rd = SampleRegexp(os.path.join("(?P<PU>[0-9]+)_(?P<SM>[a-z]+)"))
        assert rd.pattern == "(?P<PU>[0-9]+)_(?P<SM>[a-z]+)"
        assert rd.basename_pattern == "(?P<PU>[0-9]+)_(?P<SM>[a-z]+)"
        
class TestSampleRegexp:
    def test_sampleregexp_init_empty(self):
        with pytest.raises(TypeError):
            rd = SampleRegexp()

    def test_sampleregexp_missing_required_key(self):
        with pytest.raises(MissingRequiredKeyException):
            rd = SampleRegexp("(?:[A-Z0-9]+)_(?P<PATH>[0-9]+)")
    
    def test_sampleregexp_parse_unable(self):
        rd = SampleRegexp("(?:[A-Z0-9]+)_(?P<SM>[A-Za-z0-9]+)")
        assert rd.parse("bar/foo_007") == {}

    def test_sampleregexp_wrong_indexed_key(self):
        with pytest.raises(DisallowedKeyException):
            rd = SampleRegexp("(?:[A-Z0-9]+)_(?P<SM>[0-9]+)_(?P<ID1>[0-9]+)")

    def test_sampleregexp_correct_indexed_key(self):
        rd = SampleRegexp(os.path.join("(?P<SM>[A-Za-z0-9]+)", "(?:[A-Z0-9]+)_(?P<PU2>[0-9]+)_(?P<PU1>[0-9]+)"))
        assert rd.fmt == "{SM}/{PU2}_{PU1}"
        rd.parse("BAR/FOO_007_1")
        assert rd == {'PATH': 'BAR', 'PU': '1_007', 'PU2': '007', 'PU1': '1', 'SM' : 'BAR'}

class TestGroupBy:
    def test_list(self):
        r = re.compile("(?P<SM>[A-Z0-9]+)_(?P<ID2>[0-9]+)_(?P<ID1>[0-9]+)")
        keymap = sorted([(re.sub("[0-9]+$", "", k), k)  if re.search("[0-9]+$", k) else (k, k) for k in list(r.groupindex.keys())])
        _keymap = {k:[y[1] for y in list(v)] for (k,v) in groupby(keymap, lambda x: x[0])}
        assert _keymap == {'ID': ['ID1', 'ID2'], 'SM': ['SM']}

    def test_make_format(self):
        """Convert named group to format tags.

        From (?P<SM>[A-Z0-9]+)/(?P=SM)_(?P<ID2>[0-9]+)_(?P<ID1>[0-9]+) generate {SM}/{SM}_{ID2}_{ID1}"""
        r = re.compile(os.path.join("(?P<SM>[A-Z0-9]+)", "(?P=SM)_(?P<ID2>[0-9]+)_(?P<ID1>[0-9]+)"))
        m = re.findall("(\(\?P[<=](\w+)>?|({sep}))".format(sep=os.sep), r.pattern)
        fmt = re.sub("_{sep}_".format(sep=os.sep), os.sep, ("_".join("{" + x[1] + "}"  if x[1] else x[2] for x in m)))
        assert fmt == "{SM}/{SM}_{ID2}_{ID1}"

    def test_make_format_with_string(self):
        """Convert named group to format tags, including constant patterns.

        From (?P<SM>P[0-9]+_[0-9]+)/Prefix_(?P=SM)_(?P<ID2>[0-9]+)_(?P<ID1>[0-9]+) generate {SM}/Prefix_{SM}_{ID2}_{ID1}"""
        r = re.compile(os.path.join("(?P<SM>P[0-9]+_[0-9]+)", "Prefix_(?P=SM)_(?P<ID2>[0-9]+)_(?P<ID1>[0-9]+)"))
        m = re.findall("(\(\?P[<=](\w+)>?\w*\)?|({sep})|(?:\[[A-Za-z0-9\-]+\])|([A-Za-z0-9]+))".format(sep=os.sep), r.pattern)
        fmtlist = []
        for x in m:
            if x[1]:
                fmtlist.append("{" + x[1] + "}")
            elif x[2]:
                fmtlist.append(x[2])
            elif x[3]:
                fmtlist.append(x[3])
        fmt = re.sub("_{sep}_".format(sep=os.sep), os.sep, ("_".join(fmtlist)))
        assert fmt == "{SM}/Prefix_{SM}_{ID2}_{ID1}"
        
    def test_make_format_run_id(self):
        """Convert named group to format tags, including constant patterns. Emulate raw_run_re.

        From (?P<SM>P[0-9]+_[0-9]+)/(?P<DT>[0-9]+)_(?P<PU1>[A-Z0-9+]XX)/Prefix_(?P<PU2>[0-9])_(?P=DT)_(?P=PU1)_(?P=SM) generate {SM}/{DT}_{PU1}/Prefix_{PU2}_{DT}_{PU1}_{SM}"""
        r = re.compile("(?P<SM>P[0-9]+_[0-9]+)/(?P<DT>[0-9]+)_(?P<PU1>[A-Z0-9+]XX)/Prefix_(?P<PU2>[0-9])_(?P=DT)_(?P=PU1)_(?P=SM)")
        m = re.findall("(\(\?P[<=](\w+)>?|({sep})|(?:[\[\]A-Za-z0-9\-\+\_]+\))|([A-Za-z0-9]+))".format(sep=os.sep), r.pattern)
        fmtlist = []
        for x in m:
            if x[1]:
                fmtlist.append("{" + x[1] + "}")
            elif x[2]:
                fmtlist.append(x[2])
            elif x[3]:
                fmtlist.append(x[3])
        fmt = re.sub("_{sep}_".format(sep=os.sep), os.sep, ("_".join(fmtlist)))
        assert fmt == "{SM}/{DT}_{PU1}/Prefix_{PU2}_{DT}_{PU1}_{SM}"

class TestReadGroup:
    """Test ReadGroup class"""
    def test_rg_init(self):
        """Test initializing ReadGroup"""
        rg = ReadGroup("(?P<ID>[A-Za-z0-9]+)", ID='test', DT="120924")
        assert str(rg) == '--date 2012-09-24 --identifier test'
        rg = ReadGroup("(?P<ID>[A-Za-z0-9]+)", **{'ID':'test', 'DT':"120924"})
        assert str(rg) == '--date 2012-09-24 --identifier test'
        
    def test_rg_parse_illumina_like(self):
        """Test parsing illumina-like-based file names"""
        rg = ReadGroup("(?P<SM>[a-zA-Z0-9_]+)/(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)/(?P<PU1>[0-9])_(?P=DT)_(?P=PU2)_(?P=SM)")
        rg.parse("../data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz")
        assert "--date 2012-10-15 --identifier 1_121015_BB002BBBXX_P001_101 --platform-unit 1_BB002BBBXX --sample P001_101" == str(rg)

    def test_rg_fn(self):
        """Test initializing read group class and setting function"""
        rg_fn = ReadGroup("(?P<PU1>[0-9])_(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P<SM>P[0-9]+_[0-9]+)").parse
        s = rg_fn("../data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz")
        assert "--date 2012-10-15 --identifier 1_121015_BB002BBBXX_P001_101 --platform-unit 1_BB002BBBXX --sample P001_101" == str(s)

    def test_rg_disallowed_key(self):
        """Test setting a read group object with a key not present in allowed keys"""
        with pytest.raises(DisallowedKeyException):
            rg = ReadGroup("(?P<PU1>[0-9])_(?P<DATE>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P<SM>P[0-9]+_[0-9]+)")
            s = (rg.parse("../data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz"))




# NB: all regexp names must be relative, and complete, to the working
# directory. IOW, the target generator must return paths of this
# format. Still, test full path names below just to make sure we catch
# anomalous cases.
class TestParseFunctionality:
    @pytest.fixture(scope="class")
    def data(self, request):
        return {'re': r"(?P<SM>\w+)/(?P<PU>[A-Za-z0-9_]+)/(?P<PU1>[0-9])_(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P=SM)",
                'full_re': r"(?:[\.\w\/]+)?\/(?P<SM>\w+)/(?P<PU>[A-Za-z0-9_]+)/(?P<PU1>[0-9])_(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P=SM)",
                'fn':  "P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz",
                'full_fn': "../data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz"
        }

    def test_relpath(self, data):
        m = re.search(data['re'], data['fn'])
        assert m.groupdict() == {'SM': 'P001_101', 'DT': '121015', 'PU1': '1', 'PU2': 'BB002BBBXX', 'PU': '121015_BB002BBBXX'}

    def test_curdir_path(self, data):
        m = re.search(data['full_re'], os.path.join(os.curdir, data['fn']))
        assert m.groupdict() == {'SM': 'P001_101', 'DT': '121015', 'PU1': '1', 'PU2': 'BB002BBBXX', 'PU': '121015_BB002BBBXX'}
        
    def test_pardir_path(self, data):
        m = re.search(data['full_re'], data['full_fn'])
        assert m.groupdict() == {'SM': 'P001_101', 'DT': '121015', 'PU1': '1', 'PU2': 'BB002BBBXX', 'PU': '121015_BB002BBBXX'}
        
    def test_abspath(self, data):
        m = re.search(data['full_re'], os.path.abspath(data['full_fn']))
        assert m.groupdict() == {'SM': 'P001_101', 'DT': '121015', 'PU1': '1', 'PU2': 'BB002BBBXX', 'PU': '121015_BB002BBBXX'}

    def test_pardir(self, mocker):
        mock_re = mocker.patch('snakemakelib.sample.regexp.re.match')
        mock_re.return_value = None
        rg = ReadGroup("(?P<SM>[a-zA-Z0-9]+)/(?P<PU>[A-Za-z0-9]+)/(?P<PU1>[0-9])_(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P=SM)")
        rg.parse("../data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz", "")
        (args, kw) = mock_re.call_args
        assert args[0].startswith('(?:[\\.\\w\\/]+)?\\/')

    def test_curdir(self, mocker):
        mock_re = mocker.patch('snakemakelib.sample.regexp.re.match')
        mock_re.return_value = None
        rg = ReadGroup(r"(?P<SM>[a-zA-Z0-9]+)/(?P<PU>[A-Za-z0-9]+)/(?P<PU1>[0-9])_(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P=SM)")
        rg.parse("./data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz", "")
        (args, kw) = mock_re.call_args
        assert args[0].startswith('(?:[\\.\\w\\/]+)?\\/')

    def test_os_sep(self, mocker):
        mock_re = mocker.patch('snakemakelib.sample.regexp.re.match')
        mock_re.return_value = None
        rg = ReadGroup("(?P<SM>[a-zA-Z0-9]+)/(?P<PU>[A-Za-z0-9]+)/(?P<PU1>[0-9])_(?P<DT>[0-9]+)_(?P<PU2>[A-Z0-9]+XX)_(?P=SM)")
        rg.parse("/data/projects/J.Doe_00_01/P001_101/121015_BB002BBBXX/1_121015_BB002BBBXX_P001_101_1.fastq.gz", "")
        (args, kw) = mock_re.call_args
        assert args[0].startswith('(?:[\\.\\w\\/]+)?\\/')
