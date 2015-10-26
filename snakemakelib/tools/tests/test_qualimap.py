# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103
import pytest
import pandas as pd
from ..qualimap import Qualimap
import snakemakelib.results

@pytest.fixture(scope="module", autouse=True)
def qualimap():
    return ['>>>>>>> Globals\n',
            'number of windows = 10\n',
            'number of reads = 10,000,000\n',
            'number of mapped reads = 9,900,000 (99.00%)\n',
            'number of duplicated reads = 400,000\n\n',
            '>>>>>>> Insert size\n',
            '>>>>>>> Coverage per contig\n',
            '\n',
            '\t'.join(['foo', '11', '12', '1.1', '1.2\n']),
            '\t'.join(['bar', '21', '22', '2.1', '2.2\n'])]

def mockreturn(cls, f):
    return qualimap()

def test_qualimap_coverage(monkeypatch):
    monkeypatch.setattr(snakemakelib.results.Results, 'load_lines', mockreturn)
    qm = Qualimap([('foo', 'bar')])
    assert [34.375, 65.625] == list(qm['coverage_per_contig']['chrlen_percent'])

def test_qualimap_globals(monkeypatch):
    monkeypatch.setattr(snakemakelib.results.Results, 'load_lines', mockreturn)
    qm = Qualimap([('foo', 'bar')])
    assert sorted([10.0, 400000.0, 9500000.0, 10000000.0, 9900000.0]) == sorted(list(qm['globals'].loc['bar']))

def test_collect_results(qualimap, monkeypatch, mocker):
    monkeypatch.setattr(snakemakelib.results.Results, 'load_lines', mockreturn)
    mock_df = mocker.patch('pandas.DataFrame')
    Qualimap([('foo', 'bar')])
    (args, kw) = mock_df.call_args
    assert [x.strip("\n").split("\t") for x in qualimap[8:]] ==  args[0]
