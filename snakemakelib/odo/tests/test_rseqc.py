# Copyright (C) 2015 by Per Unneberg
import os
from blaze import DataFrame, odo
from snakemakelib.odo import rseqc
import pytest


@pytest.fixture(scope="module")
def rseqc_read_distribution(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('read_distribution.txt')
    fn.write("""processing annotation.bed12 ... Done
processing input.bam ... Finished

Total Reads                   12320102
Total Tags                    14195818
Total Assigned Tags           12271869
=====================================================================
Group               Total_bases         Tag_count           Tags/Kb             
CDS_Exons           0                   0                   0.00              
5'UTR_Exons         45222079            2206164             48.79             
3'UTR_Exons         45490871            7852006             172.61            
Introns             965973054           2022848             2.09              
TSS_up_1kb          26441266            8084                0.31              
TSS_up_5kb          120694350           41844               0.35              
TSS_up_10kb         218600112           47083               0.22              
TES_down_1kb        27629376            21857               0.79              
TES_down_5kb        120559498           112882              0.94              
TES_down_10kb       214667322           143768              0.67              
=====================================================================
""")
    return fn


@pytest.fixture(scope="module")
def rseqc_read_distribution2(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data2').join('read_distribution.txt')
    fn.write("""processing annotation.bed12 ... Done
processing input.bam ... Finished

Total Reads                   12320102
Total Tags                    14195818
Total Assigned Tags           12271869
=====================================================================
Group               Total_bases         Tag_count           Tags/Kb             
CDS_Exons           0                   0                   0.00              
5'UTR_Exons         45222079            2206164             48.79             
3'UTR_Exons         45490871            7852006             172.61            
Introns             965973054           2022848             2.09              
TSS_up_1kb          26441266            8084                0.31              
TSS_up_5kb          120694350           41844               0.35              
TSS_up_10kb         218600112           47083               0.22              
TES_down_1kb        27629376            21857               0.79              
TES_down_5kb        120559498           112882              0.94              
TES_down_10kb       214667322           143768              0.67              
=====================================================================
""")
    return fn


def test_rseqc_read_distribution(rseqc_read_distribution):
    df = odo(str(rseqc_read_distribution), DataFrame)
    assert "TES_down_10kb" in df.index
    assert df.loc["Introns", "Tag_count"] == 2022848
    

# Proof of principle of globbing functionality
def test_rseqc_glob(rseqc_read_distribution, rseqc_read_distribution2):
    df = odo(os.path.join(os.path.dirname(os.path.dirname(str(rseqc_read_distribution))), "*/*distribution.txt"), DataFrame)
    assert df.shape == (20,3)
