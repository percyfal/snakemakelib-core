# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
import logging
import pytest
from snakemakelib.results import Results
from snakemakelib.exceptions import SamplesException, OutputFilesException
from snakemakelib.regexp import RunRegexp
logging.basicConfig(level=logging.DEBUG)

class Foo(Results):
    _keys = ['foo', 'bar']

    def __init__(self, *args, **kw):
        super(Foo, self).__init__(*args, **kw)

    def _collect_results(self):
        pass

@pytest.fixture(scope="module")
def f():
    return Foo(inputs=[("foo", "bar"), ("foofoo", "barbar")])

class TestResults:
    """Test results base class"""
    def test_base_init(self):
        with pytest.raises(NotImplementedError):
            Results()

    def test_init_wrong_inputs(self):
        with pytest.raises(TypeError):
            Results(inputs=["foo", "bar"])

    def test_init(self):
        Foo()

    def test_init_inputs_and_samples(self):
        Foo(inputs=["foo", "bar"], samples=["foofoo", "barbar"])

    def test_init_args(self):
        Foo(inputs=[("foo", "bar"),
                    ("foofoo", "barbar")])

    def test_init_wrong_regexp(self):
        with pytest.raises(Exception):
            Foo(inputs=("foofile", "barfile"),
                re=RunRegexp(r"(\w+)"))

    def test_init_regexp(self):
        Foo(inputs=("foofile", "barfile"),
            re=RunRegexp(r"(?P<SM>[\w]+)file"))

    def test_init_inputs_wrong_samples(self):
        with pytest.raises(SamplesException):
            Foo(inputs=["foo"], samples=["foofoo", "barbar"])

    def test_save_wrong_outputs(self, f):
        with pytest.raises(OutputFilesException):
            f.save([])

    def test_save(self, f, mocker):
        mock_to_csv = mocker.patch('pandas.DataFrame.to_csv')
        f.save(["f", "b"])

    def test_parse1(self, f, mocker):
        mock_parse = mocker.patch('pandas.DataFrame')
        f.parse_data([["foo", "bar"],
                      ["foofoo", "barbar"]])
        (args, _) = mock_parse.call_args
        assert [["foo", "bar"], ["foofoo", "barbar"]] ==  args[0]

    def test_parse2(self, f, mocker):
        mock_parse = mocker.patch('pandas.DataFrame')
        f.parse_data([["foo", "bar"],
                      ["foofoo", "barbar"]],
                     rs=("foo", None))
        (args, _) = mock_parse.call_args
        assert [["foo", "bar"], ["foofoo", "barbar"]] == args[0]

    def test_parse3(self, f, mocker):
        mock_parse = mocker.patch('pandas.DataFrame')
        f.parse_data([["foo", "bar"],
                      ["foofoo", "barbar"]],
                     rs=(None, "barbar"))
        (args, _) = mock_parse.call_args
        assert [["foo", "bar"]] == args[0]

    def test_parse4(self, f, mocker):
        mock_parse = mocker.patch('pandas.DataFrame')
        f.parse_data([["foo", "bar"],
                      ["foofoo", "barbar"]],
                     rs=(None, None), skip=1)
        (args, _) = mock_parse.call_args
        assert [["foofoo", "barbar"]] == args[0]

    def test_load_data_frame(self, mocker):
        mock_read_csv = mocker.patch('pandas.read_csv')
        f = Foo(inputs=[("foo", "bar"), ("foofoo", "barbar")])
        f.load_data_frame("foo")
        (args, kw) = mock_read_csv.call_args
        assert ('foo',) == args
