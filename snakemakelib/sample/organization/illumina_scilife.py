# Copyright (C) 2015 by Per Unneberg
"""The ``illumina_scilife`` module defines sample organization for
dealing with data delivered by the `NGI Stockholm (Genomics
Production)
<https://www.scilifelab.se/facilities/genomics-production/>`_
sequencing platform hosted at `SciLifeLab
<https://www.scilifelab.se/>`_. The sample organization is defined as
follows:

raw_run_re
  ``IOTarget(os.path.join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU1, [A-Z0-9]+XX}", "{PU2, [0-9]}_{DT}_{PU1}_{SM}"))``
run_id_re
  ``IOTarget(os.path.join("{SM, P[0-9]+_[0-9]+}", "{DT,[0-9]+}_{PU1,[A-Z0-9]+XX}", "{PU2,[0-9]}_{DT}_{PU1}_{SM}"))``
sample_re
  ``IOSampleTarget(os.path.join("{SM,P[0-9]+_[0-9]+}", "{SM}"))``


Details
^^^^^^^^

The delivery note carries the following information on naming
conventions:

  The data is delivered in fastq format using Illumina 1.8 quality
  scores. There will be one file for the forward reads and one file for
  the reverse reads (if the run was a paired-end run). The naming of the
  files follow the convention: [LANE]_[DATE]_[FLOWCELL]_[SCILIFENAME]_[READ].fastq.gz

In addition, fastq files are delivered into directories with the
structure [SCILIFENAME]/[DATE]_[FLOWCELL]. Equating SCILIFENAME with
sample, the top directory corresponds to the sample, and a
subdirectory to a specific flowcell run. The entire file name
including directory structure is therefore

  [SCILIFENAME]/[DATE]_[FLOWCELL]/[LANE]_[DATE]_[FLOWCELL]_[SCILIFENAME]_[READ].fastq.gz

The following translation table relate the tags to the read group tags:

===============               ================
Read group tag                Tag
===============               ================
SM                            SCILIFENAME
DT                            DATE
PU1                           FLOWCELL
PU2                           LANE
PU                            FLOWCELL_LANE
===============               ================

The platform unit tags PU1 and PU2 are concatenated to produce a PU
tag.
"""
from . import update_config, config, SampleOrganization, join, IOTarget, IOSampleTarget

update_config(
    config, {'settings': {
        'sample_organization': SampleOrganization(IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT, [0-9]+}_{PU1, [A-Z0-9]+XX}", "{PU2, [0-9]}_{DT}_{PU1}_{SM}")),
                                          IOTarget(join("{SM, P[0-9]+_[0-9]+}", "{DT,[0-9]+}_{PU1,[A-Z0-9]+XX}", "{PU2,[0-9]}_{DT}_{PU1}_{SM}")),
                                          IOSampleTarget(join("{SM,P[0-9]+_[0-9]+}", "{SM}")))}})
