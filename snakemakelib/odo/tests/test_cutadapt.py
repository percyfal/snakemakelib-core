# Copyright (C) 2015 by Per Unneberg
from blaze import DataFrame, odo
from snakemakelib.odo import cutadapt
import pytest

@pytest.fixture(scope="module")
def cutadapt_se_data(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('single_end.cutadapt_metrics')
    fn.write("""This is cutadapt 1.8.3 with Python 2.7.10
Command line parameters: -q 20,20 --trim-n --max-n=2 -m 50 1_120924_AC003CCCXX_P001_101_1.fastq.gz -b file:adapters.fa -o 1_120924_AC003CCCXX_P001_101.trimmed_1.fastq.gz
Trimming 2 adapters with at most 10.0% errors in single-end mode ...
Finished in 0.05 s (50 us/read; 1.20 M reads/minute).

=== Summary ===

Total reads processed:                   1,001
Reads with adapters:                        54 (5.4%)
Reads that were too short:                  68 (6.8%)
Reads with too many N:                       0 (0.0%)
Reads written (passing filters):           933 (93.2%)

Total basepairs processed:        76,076 bp
Quality-trimmed:                   4,930 bp (6.5%)
Total written (filtered):         69,580 bp (91.5%)

=== Adapter 'i7_adapter_5p_3p' ===

Sequence: CAAGCAGAAGACGGCATACGAGATNNNNNNNNGTCTCGTGGGCTCGG; Type: variable 5'/3'; Length: 47; Trimmed: 34 times.
10 times, it overlapped the 5' end of a read
24 times, it overlapped the 3' end or was within the read

No. of allowed errors:
0-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-39 bp: 3; 40-47 bp: 4

Overview of removed sequences (5')
length	count	expect	max.err	error counts
3	4	15.6	0	4
4	4	3.9	0	4
5	1	1.0	0	1
7	1	0.1	0	1


Overview of removed sequences (3' or within)
length	count	expect	max.err	error counts
3	19	15.6	0	19
4	4	3.9	0	4
5	1	1.0	0	1

=== Adapter 'i7_adapter_5p_3p_Reversed:' ===

Sequence: CCGAGCCCACGAGACNNNNNNNNATCTCGTATGCCGTCTTCTGCTTG; Type: variable 5'/3'; Length: 47; Trimmed: 20 times.
14 times, it overlapped the 5' end of a read
6 times, it overlapped the 3' end or was within the read

No. of allowed errors:
0-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-39 bp: 3; 40-47 bp: 4

Overview of removed sequences (5')
length	count	expect	max.err	error counts
3	11	15.6	0	11
4	2	3.9	0	2
9	1	0.0	0	1


Overview of removed sequences (3' or within)
length	count	expect	max.err	error counts
3	6	15.6	0	6

""")
    return fn


@pytest.fixture(scope="module")
def cutadapt_pe_data(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('paired_end.cutadapt_metrics')
    fn.write("""This is cutadapt 1.8.3 with Python 2.7.10
Command line parameters: -q 20,20 --trim-n --max-n=2 -m 50 1_120924_AC003CCCXX_P001_101_1.fastq.gz 1_120924_AC003CCCXX_P001_101_2.fastq.gz -b file:adapters.fa -B file:adapters.fa -o 1_120924_AC003CCCXX_P001_101.trimmed_1.fastq.gz -p 1_120924_AC003CCCXX_P001_101.trimmed_2.fastq.gz
Trimming 4 adapters with at most 10.0% errors in paired-end mode ...
Finished in 0.11 s (110 us/read; 0.55 M reads/minute).

=== Summary ===

Total read pairs processed:              1,001
  Read 1 with adapter:                      54 (5.4%)
  Read 2 with adapter:                      45 (4.5%)
Pairs that were too short:                 107 (10.7%)
Pairs with too many N:                       0 (0.0%)
Pairs written (passing filters):           894 (89.3%)

Total basepairs processed:       152,152 bp
  Read 1:        76,076 bp
  Read 2:        76,076 bp
Quality-trimmed:                   9,556 bp (6.3%)
  Read 1:         4,930 bp
  Read 2:         4,626 bp
Total written (filtered):        134,002 bp (88.1%)
  Read 1:        66,777 bp
  Read 2:        67,225 bp

=== First read: Adapter 'i7_adapter_5p_3p' ===

Sequence: CAAGCAGAAGACGGCATACGAGATNNNNNNNNGTCTCGTGGGCTCGG; Type: variable 5'/3'; Length: 47; Trimmed: 34 times.
10 times, it overlapped the 5' end of a read
24 times, it overlapped the 3' end or was within the read

No. of allowed errors:
0-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-39 bp: 3; 40-47 bp: 4

Overview of removed sequences (5')
length	count	expect	max.err	error counts
3	4	15.6	0	4
4	4	3.9	0	4
5	1	1.0	0	1
7	1	0.1	0	1


Overview of removed sequences (3' or within)
length	count	expect	max.err	error counts
3	19	15.6	0	19
4	4	3.9	0	4
5	1	1.0	0	1

=== First read: Adapter 'i7_adapter_5p_3p_Reversed:' ===

Sequence: CCGAGCCCACGAGACNNNNNNNNATCTCGTATGCCGTCTTCTGCTTG; Type: variable 5'/3'; Length: 47; Trimmed: 20 times.
14 times, it overlapped the 5' end of a read
6 times, it overlapped the 3' end or was within the read

No. of allowed errors:
0-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-39 bp: 3; 40-47 bp: 4

Overview of removed sequences (5')
length	count	expect	max.err	error counts
3	11	15.6	0	11
4	2	3.9	0	2
9	1	0.0	0	1


Overview of removed sequences (3' or within)
length	count	expect	max.err	error counts
3	6	15.6	0	6

=== Second read: Adapter 'i7_adapter_5p_3p' ===

Sequence: CAAGCAGAAGACGGCATACGAGATNNNNNNNNGTCTCGTGGGCTCGG; Type: variable 5'/3'; Length: 47; Trimmed: 29 times.
9 times, it overlapped the 5' end of a read
20 times, it overlapped the 3' end or was within the read

No. of allowed errors:
0-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-39 bp: 3; 40-47 bp: 4

Overview of removed sequences (5')
length	count	expect	max.err	error counts
3	3	15.6	0	3
4	2	3.9	0	2
5	1	1.0	0	1
7	2	0.1	0	2
10	1	0.0	1	0 1


Overview of removed sequences (3' or within)
length	count	expect	max.err	error counts
3	18	15.6	0	18
4	2	3.9	0	2

=== Second read: Adapter 'i7_adapter_5p_3p_Reversed:' ===

Sequence: CCGAGCCCACGAGACNNNNNNNNATCTCGTATGCCGTCTTCTGCTTG; Type: variable 5'/3'; Length: 47; Trimmed: 16 times.
12 times, it overlapped the 5' end of a read
4 times, it overlapped the 3' end or was within the read

No. of allowed errors:
0-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-39 bp: 3; 40-47 bp: 4

Overview of removed sequences (5')
length	count	expect	max.err	error counts
3	6	15.6	0	6
4	5	3.9	0	5
6	1	0.2	0	1


Overview of removed sequences (3' or within)
length	count	expect	max.err	error counts
3	3	15.6	0	3
4	1	3.9	0	1

""")
    return fn
             
def test_cutadapt_se(cutadapt_se_data):
    df = odo(str(cutadapt_se_data), DataFrame)
    assert df.loc["Reads with adapters"]["value"] == 54

def test_cutadapt_pe(cutadapt_pe_data):
    df = odo(str(cutadapt_pe_data), DataFrame)
    assert df.loc["Read 1 with adapter"]["value"] == 54
    assert list(df.loc["Read 1"]["value"]) == [76076, 4930, 66777]

