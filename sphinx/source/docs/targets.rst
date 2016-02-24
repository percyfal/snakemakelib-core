.. _snakemakelib_core.targets:

Targets and applications
=========================

Finding input
--------------

.. _snakemakelib_core.targets.iotarget:

The IOTarget class
-------------------

The :class:`~snakemakelib.io.IOTarget` class provides a means to
define what the input looks like. It is modeled on the
:class:`snakemake.io.IOFile` class which uses python mini format
strings to setup regular expressions for string matching.

.. code-block:: text

   2_141414_AOXX.fastq.gz

   LANE_FLOWCEL

.. _snakemakelib_core.targets.applications:

Applications - grouping IOTargets together
-------------------------------------------

