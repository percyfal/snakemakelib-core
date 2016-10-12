from collections import namedtuple
from . import IOTarget, IOSampleTarget

class SampleOrganization(namedtuple('SampleOrganization', 'raw_run_re run_id_re sample_re')):
    """
Collect :class:`~snakemakelib.io.IOTarget` objects for organization
of input/output file names

Subclasses :py:class:`collections.namedtuple`. In the current
implementation, three levels of organization are defined.

Raw data
  This corresponds to the file format as delivered from sequencing facility or the like
Run id
  This corresponds to files at the run level (platform unit level)
Sample
  This corresponds to files at the sample level

Args:
  raw_run_re (IOTarget): raw run prefix. This corresponds to the file format as delivered from sequencing facility or the like
  run_id_re (IOTarget): run id prefix. Identifies files at the run level (platform unit). This may or may not be different from ``raw_run_re``
  sample_re (IOSampleTarget): sample prefix. Prefix used to identify result files on the sample level.
    """
    __slots__ = ()

    def __new__(cls, raw_run_re, run_id_re, sample_re):
        assert isinstance(raw_run_re, IOTarget), "raw_run_re is not an IOTarget: {}".format(type(raw_run_re))
        assert isinstance(run_id_re, IOTarget), "run_id_re is not an IOTarget: {}".format(type(run_id_re))
        assert isinstance(sample_re, IOSampleTarget), "sample_re is not an IOSampleTarget: {}".format(type(sample_re))
        return super(cls, SampleOrganization).__new__(cls, raw_run_re, run_id_re, sample_re)
