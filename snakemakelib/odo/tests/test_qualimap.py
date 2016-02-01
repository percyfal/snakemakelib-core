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


@pytest.fixture(scope="module")
def qualimap_data_2_1_3(tmpdir_factory):
    fn = tmpdir_factory.mktemp('test.bam.qualimap').join('genome_results.txt')
    fn.write("""BamQC report
-----------------------------------

>>>>>>> Input

     bam file = test.bam
     outfile = /home/peru/dev/snakemake-rules/snakemake_rules/tests/data/test_stats/genome_results.txt


>>>>>>> Reference

     number of bases = 2,000,000 bp
     number of contigs = 1


>>>>>>> Globals

     number of windows = 400

     number of reads = 50
     number of mapped reads = 50 (100%)

     number of mapped paired reads (first in pair) = 25
     number of mapped paired reads (second in pair) = 25
     number of mapped paired reads (both in pair) = 50
     number of mapped paired reads (singletons) = 0

     number of mapped bases = 3,795 bp
     number of sequenced bases = 3,793 bp
     number of aligned bases = 0 bp
     number of duplicated reads (estimated) = 0
     duplication rate = 0%


>>>>>>> Insert size

     mean insert size = 173.32
     std insert size = 76.98
     median insert size = 155


>>>>>>> Mapping quality
     mean mapping quality = 0.3


>>>>>>> ACTG content

     number of A's = 971 bp (25.6%)
     number of C's = 999 bp (26.34%)
     number of T's = 868 bp (22.88%)
     number of G's = 955 bp (25.18%)
     number of N's = 0 bp (0%)

     GC percentage = 51.52%


>>>>>>> Mismatches and indels

    general error rate = 0.01
    number of mismatches = 26


>>>>>>> Coverage

     mean coverageData = 0X
     std coverageData = 0.16X

     There is a 0.03% of reference with a coverageData >= 1X
     There is a 0.02% of reference with a coverageData >= 2X
     There is a 0.02% of reference with a coverageData >= 3X


>>>>>>> Coverage per contig

        chr11   2000000 3795    0.0018975       0.15562423747202747

""")
    return fn


def test_qualimap(qualimap_data):
    df = odo(str(qualimap_data), DataFrame, key='Coverage_per_contig')
    assert list(df.columns) == ['chrlen', 'mapped_bases', 'mean_coverage', 'sd']
    assert list(df.index) == ['chr10', 'chr11']


def test_qualimap_2_1_3(qualimap_data_2_1_3):
    df = odo(str(qualimap_data_2_1_3), DataFrame, key='Coverage_per_contig')
    assert list(df.columns) == ['chrlen', 'mapped_bases', 'mean_coverage', 'sd']
    assert list(df.index) == ['chr11']
