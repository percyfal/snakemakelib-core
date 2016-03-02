from collections import namedtuple

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
  sample_re (IOTarget): sample prefix. Prefix used to identify result files on the sample level.


Returns:
  Sample organization object (:class:`snakemakelib.sample.organization.SampleOrganization`)
    """


    raw_run_re = None
    """Test doc for raw_run_re"""

    run_id_re = None
    """Test doc for run_id_re"""

    sample_re = None
    """Test doc for sample_re"""

