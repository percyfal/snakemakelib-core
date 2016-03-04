# Copyright (C) 2015 by Per Unneberg
"""The ``sample_run_sra`` module defines sample organization for
dealing with data from the `Sequence Read Archive
<http://www.ncbi.nlm.nih.gov/sra>`_. The sample organization is
defined as follows:

raw_run_re
  ``IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}", "{PU}")``
run_id_re
  ``IOTarget(os.path.join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}", "{PU}")``
sample_re
  ``IOSampleTarget(os.path.join("{SM,[a-zA-Z0-9]+}", "{SM}"))``


Details
^^^^^^^^^

A specific sequencing run is identified by a specific `SRA accession
type
<http://www.ncbi.nlm.nih.gov/books/NBK56913/#search.what_do_the_different_sra_accessi>`_,
where the interesting one from a sample organization perspective is
the Sequencing Run Accession (SRR). The SRR is associated with the PU
read group tag, where each sequencing run resides in a separate
subdirectory of a sample. The sample is often identified by the `GEO
accession number
<http://www.ncbi.nlm.nih.gov/geo/info/overview.html>`_.

There is a `rule for downloading srastudy metadata
<https://github.com/percyfal/snakemake-rules/blob/master/snakemake_rules/bio/ngs/tools/sratools.rules>`_
in the `snakemake-rules
<https://github.com/percyfal/snakemake-rules>`_. Typically, the
downloaded metadata will consist of a csv file with the run identified
by the ``Run`` column, and sample by the ``source`` column, if
present.

"""
from . import update_config, config, SampleOrganization, join, IOTarget, IOSampleTarget

update_config(
    config, {'settings': {
        'sample_organization': SampleOrganization(IOTarget(join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}", "{PU}")),
                                                  IOTarget(join("{SM, [a-zA-Z0-9]+}", "{PU, [a-zA-Z0-9]+}", "{PU}")),
                                                  IOSampleTarget(join("{SM, [a-zA-Z0-9]+}", "{SM}")))}})

