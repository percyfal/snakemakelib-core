# Copyright (C) 2015 by Per Unneberg
from blaze import DataFrame, odo
from snakemakelib.odo import xls
import io
import pytest

@pytest.fixture(scope="module")
def xlsdata(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('file.xls')
    fn.write("""Position	A	C	G	T	N	X
0	1136683	1708546	2832822	803802	10172	0
1	1233263	1759549	1149710	2349503	0	0
2	1443419	1933820	1319547	1795239	0	0
3	1000759	2326980	952180	2212106	0	0
4	2285164	1018958	1063250	2124653	0	0
5	2188790	940011	2313352	1049868	4	0
6	1905443	1269657	2002775	1314150	0	0
""")
    return fn

def test_xls(xlsdata):
    df = odo(str(xlsdata), DataFrame)
    assert all(df["Position"] == range(0,7))

