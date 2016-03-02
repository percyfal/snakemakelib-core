.. _snakemakelib.sample.input:

``snakemakelib.sample.input``
================================

Functions for dealing with sample input information.


.. _snakemakelib.sample.input.utility_functions:

Utility functions
------------------

.. autofunction:: snakemakelib.sample.input.convert_samples_to_list



Input initialization
---------------------

These functions are used to generate lists of inputs to a workflow.
Input information is either read from a sampleinfo file, or parsed
directly from input file names.
		  
.. autofunction:: snakemakelib.sample.input.initialize_input
.. autofunction:: snakemakelib.sample.input._parse_sampleinfo
.. autofunction:: snakemakelib.sample.input._samples_from_input_files   
		  
