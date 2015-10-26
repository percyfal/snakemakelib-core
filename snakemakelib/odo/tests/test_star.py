# Copyright (C) 2015 by Per Unneberg
from blaze import DataFrame, odo
from snakemakelib.odo import star
import pytest

@pytest.fixture(scope="module")
def star_data(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('star.Log.final.out')
    fn.write("""                                 Started job on |       Apr 29 22:42:00
                             Started mapping on |       Apr 29 22:42:00
                                    Finished on |       Apr 29 22:43:51
       Mapping speed, Million of reads per hour |       152.43

                          Number of input reads |       4699845
                      Average input read length |       202
                                    UNIQUE READS:
                   Uniquely mapped reads number |       4011114
                        Uniquely mapped reads % |       85.35%
                          Average mapped length |       198.26
                       Number of splices: Total |       1452777
            Number of splices: Annotated (sjdb) |       1424534
                       Number of splices: GT/AG |       1429760
                       Number of splices: GC/AG |       12299
                       Number of splices: AT/AC |       1528
               Number of splices: Non-canonical |       9190
                      Mismatch rate per base, % |       0.70%
                         Deletion rate per base |       0.02%
                        Deletion average length |       1.76
                        Insertion rate per base |       0.01%
                       Insertion average length |       1.46
                             MULTI-MAPPING READS:
        Number of reads mapped to multiple loci |       267393
             % of reads mapped to multiple loci |       5.69%
        Number of reads mapped to too many loci |       7530
             % of reads mapped to too many loci |       0.16%
                                  UNMAPPED READS:
       % of reads unmapped: too many mismatches |       0.00%
                 % of reads unmapped: too short |       8.73%
                     % of reads unmapped: other |       0.08%
""")
    return fn

def test_star_log(star_data):
    df = odo(str(star_data), DataFrame)
    assert df.loc["% of reads unmapped: too short","value"] == 8.73
    assert df.loc["Uniquely mapped reads number","value"] == 4011114

