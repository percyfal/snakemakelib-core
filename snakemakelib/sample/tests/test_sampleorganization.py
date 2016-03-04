# Copyright (C) 2015 by Per Unneberg
import pytest
from snakemakelib.sample.organization import SampleOrganization, IOTarget


def test_sample_org_init():
    so = SampleOrganization(raw_run_re=IOTarget("foo"),
                            run_id_re=IOTarget("bar"),
                            sample_re=IOTarget("foobar"))



def test_sample_org_no_params():
    with pytest.raises(TypeError):
        SampleOrganization()

    
def test_sample_org_wrong_params():
    with pytest.raises(AssertionError):
        SampleOrganization(raw_run_re="foo", run_id_re="bar", sample_re=3)
        
