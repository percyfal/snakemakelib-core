# Copyright (C) 2015 by Per Unneberg
from blaze import DataFrame, odo
from snakemakelib.odo import qualimap
import pytest

@pytest.fixture(scope="module")
def qualimap_data(tmpdir_factory):
    fn = tmpdir_factory.mktemp('test.bam.qualimap').join('genome_results.txt')
    fn.write("""BamQC report
-----------------------------------

>>>>>>> Input

     bam file = test.bam
     outfile = test.bam.qualimap/genome_results.txt


>>>>>>> Reference

     number of bases = 3,099,922,541 bp
     number of contigs = 195


>>>>>>> Globals

     number of windows = 594

     number of reads = 265,153,164
     number of mapped reads = 155,590,112 (58.68%)

     number of mapped bases = 16,787,317,587 bp
     number of sequenced bases = 16,781,173,303 bp
     number of aligned bases = 0 bp
     number of duplicated reads = 66,228,874


>>>>>>> Insert size

     mean insert size = 542.88
     std insert size = 179,544.88
     median insert size = 173


>>>>>>> Mapping quality

     mean mapping quality = 26.35


>>>>>>> ACTG content

     number of A's = 4,954,993,625 bp (29.53%)
     number of C's = 3,877,035,318 bp (23.1%)
     number of T's = 4,739,554,261 bp (28.24%)
     number of G's = 3,209,590,099 bp (19.13%)
     number of N's = 0 bp (0%)

     GC percentage = 42.23%


>>>>>>> Mismatches and indels

    general error rate = 0.01
    number of mismatches = 115,369,273
    number of insertions = 20,493,390
    mapped reads with insertion percentage = 9.07%
    number of deletions = 3,790,290
    mapped reads with deletion percentage = 2.28%
    homopolymer indels = 11.28%


>>>>>>> Coverage

     mean coverageData = 5.42X
     std coverageData = 530.41X

     There is a 85.67% of reference with a coverageData >= 1X
     There is a 74.85% of reference with a coverageData >= 2X
     There is a 60.63% of reference with a coverageData >= 3X

>>>>>>> Coverage per contig

	chr10	133797422	566593996	4.234715344515382	52.363607372259494
	chr11	135086622	595589765	4.408947060649721	500.43918642995004



""")
    return fn

def test_qualimap(qualimap_data):
    df = odo(str(qualimap_data), DataFrame, key='Coverage_per_contig')
    assert list(df.columns) == ['chrlen', 'mapped_bases', 'mean_coverage', 'sd']
    assert list(df.index) == ['chr10', 'chr11']
