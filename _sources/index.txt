.. snakemakelib documentation master file, created by
   sphinx-quickstart on Wed Oct 14 10:19:39 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

snakemakelib-core - core functionality of snakemakelib
======================================================


.. _about:

`snakemakelib` core functionality. Adds modules, functions and
utilities for working with `Snakemake
<https://bitbucket.org/johanneskoester/snakemake/wiki/Home>`__ and
`snakemake-rules <https://github.com/percyfal/snakemake-rules>`__.

Features
^^^^^^^^

1. **IOTarget classes**. :ref:`IOTarget
   <snakemakelib_core.targets.iotarget>` classes utilize the power of
   regular expressions to find input and define output targets.
2. **Application classes**. :ref:`Application
   <snakemakelib_core.targets.applications>` classes group targets at the
   application level.
3. **Application hooks**. :ref:`Hooks <snakemakelib_core.targets.hooks>`
   makes it easy to add custom functionality, such as plot and annotation
   functions, to applications.
4. **odo parsers**. `odo <http://odo.pydata.org/en/latest/>`__ parsers
   are used for parsing program outputs, thereby making it easy to
   transform between many data formats
5. **bokeh plots**. Customized `bokeh
   <http://bokeh.pydata.org/en/latest/>`__ plots for making
   interactive graphics


.. toctree::
   :hidden:

   docs/quickstart
   docs/targets
   docs/hooks
   docs/datahandling
   docs/tutorial
   docs/reference
   docs/release_notes
