# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103
import os
import pytest
from snakemakelib.utils import find_files, isoformat

@pytest.fixture(scope="module", autouse=True)
def walk():
    return [
            [os.curdir, ['foo', 'bar'], ['1_121023_FLOWCELL_FOO.fastq.gz', 'bar.txt']],
            ['./foo', [], ['foo.txt', '1_121023_FLOWCELL_BAR.fastq.gz']],
            ['./bar', [], ['bar.txt']],
            ]


class TestFindFiles:
    def test_find_fastq_files(self, walk, mocker):
        """Find fastq files using match"""
        mock_walk = mocker.patch('os.walk')
        mock_walk.return_value = walk
        f = find_files(regexp="\w+.fastq.gz")
        assert f == ['./1_121023_FLOWCELL_FOO.fastq.gz', './foo/1_121023_FLOWCELL_BAR.fastq.gz']

    def test_find_files_search(self, walk, mocker):
        """Find files using search"""
        mock_walk = mocker.patch('os.walk')
        mock_walk.return_value = walk
        f = find_files(regexp=".fastq", search=True)
        assert f == ['./1_121023_FLOWCELL_FOO.fastq.gz', './foo/1_121023_FLOWCELL_BAR.fastq.gz']

        
class TestUtils:
    """Test snakemakelib.utils functions"""
    def test_isoformat(self):
        """Test isoformatting function"""
        s = "120924"
        assert isoformat(s) == "2012-09-24"
