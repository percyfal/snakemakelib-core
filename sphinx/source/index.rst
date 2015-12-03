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

1. **IOTarget classes**. These classes utilize the power regular
   expressions to find input and define output targets.
2. **Application classes**. Application classes group targets at the
   application level. Hooks makes it easy to add custom functionality,
   such as plot and annotation functions.
3. **odo parsers**. `odo <http://odo.pydata.org/en/latest/>`__ parsers
   are used for parsing program outputs, thereby making it easy to
   transform between many data formats
4. **bokeh plots**. Customized `bokeh
   <http://bokeh.pydata.org/en/latest/>`__ plots for making
   interactive graphics


Contents
---------

.. toctree::
   :maxdepth: 2

   docs/quickstart
   docs/targets
   docs/datahandling
   docs/tutorial
   docs/release_notes
   docs/reference
   
.. _indices:


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

