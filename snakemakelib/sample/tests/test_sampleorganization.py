# Copyright (C) 2015 by Per Unneberg
import pytest
from snakemakelib.sample.organization import SampleOrganization, IOTarget, IOSampleTarget


def test_sample_org_init():
    so = SampleOrganization(raw_run_re=IOTarget("foo"),
                            run_id_re=IOTarget("bar"),
                            sample_re=IOSampleTarget("foobar"))
    assert isinstance(so, SampleOrganization)


def test_sample_org_init_noname():
    so = SampleOrganization(IOTarget("foo"),
                            IOTarget("bar"),
                            IOSampleTarget("foobar"))
    assert isinstance(so, SampleOrganization)


def test_sample_org_no_params():
    with pytest.raises(TypeError):
        SampleOrganization()

    
def test_sample_org_wrong_params():
    with pytest.raises(AssertionError):
        SampleOrganization(raw_run_re="foo", run_id_re="bar", sample_re=3)
        
