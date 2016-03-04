from collections import namedtuple
from . import IOTarget

class SampleOrganization(namedtuple('SampleOrganization', 'raw_run_re run_id_re sample_re')):
    """
Collect :class:`~snakemakelib.io.IOTarget` objects for organization
of input/output file names

Subclasses :py:class:`namedtuple`. In the current
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
  sample_re (IOTarget): sample prefix. Prefix used to identify result files on the sample level.
    """

    def __new__(cls, raw_run_re, run_id_re, sample_re):
        assert isinstance(raw_run_re, IOTarget)
        assert isinstance(run_id_re, IOTarget)
        assert isinstance(sample_re, IOTarget)
