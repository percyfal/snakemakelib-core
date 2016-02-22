# Copyright (c) 2014 Per Unneberg
# Modelled on bokeh setup script
# --------------------------------------------------
# Imports
# --------------------------------------------------

from __future__ import print_function

# stdlib
import os
from setuptools import setup
from os.path import realpath, dirname, relpath, join

# Extensions
import versioneer

# --------------------------------------------------
# globals and constants
# --------------------------------------------------

ROOT = dirname(realpath(__file__))

# --------------------------------------------------
# classes and functions
# --------------------------------------------------

package_data = []

def package_path(path, filters=()):
    if not os.path.exists(path):
        raise RuntimeError("packaging non-existent path: %s" % path)
    elif os.path.isfile(path):
        package_data.append(relpath(path, 'snakemakelib'))
    else:
        for path, dirs, files in os.walk(path):
            path = relpath(path, 'snakemakelib')
            for f in files:
                if not filters or f.endswith(filters):
                    package_data.append(join(path, f))

rule_suffixes = ('.rules', '.rule')

package_path(join(ROOT, 'snakemakelib'), rule_suffixes)
package_path(join(ROOT, 'snakemakelib', '_templates'))
package_path(join(ROOT, 'snakemakelib', 'static'))

scripts = []

REQUIRES = [
    'snakemake>=3.4.2',
    'blaze',
    'bokeh',
]

try:
    # Hack for readthedocs
    if not 'readthedocs' in os.path.dirname(os.path.realpath(__file__)):
        pass
    else:
        print("readthedocs in path name; assuming we're building docs @readthedocs")
        REQUIRES.append('sphinx-bootstrap-theme')
except:
    pass

# Integrating pytest with setuptools: see
# http://pytest.org/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
import sys
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


_version = versioneer.get_version()
_cmdclass = versioneer.get_cmdclass()
_cmdclass.update({'test': PyTest})
setup(
    name="snakemakelib",
    version=_version,
    cmdclass=_cmdclass,
    author="Per Unneberg",
    author_email="per.unneberg@scilifelab.se",
    description="Snakemakelib core library",
    license="MIT",
    url="http://github.com/percyfal/snakemakelib-core",
    scripts=scripts,
    packages=[
        'snakemakelib',
        'snakemakelib.tests',
        'snakemakelib.applications',
        'snakemakelib.bio',
        'snakemakelib.bio.ngs',
        'snakemakelib.bio.ngs.rnaseq',
        'snakemakelib.db',
        'snakemakelib.graphics',
        'snakemakelib.odo',
        'snakemakelib.odo.tests',
        'snakemakelib.plot',
        'snakemakelib.plot.bokeh',
        'snakemakelib.report',
        'snakemakelib.sample',
        'snakemakelib.sample.tests',
        'snakemakelib.sample.organization',
        'snakemakelib.tools',
    ],
    package_data={'snakemakelib': package_data},
    install_requires=REQUIRES,
    tests_requires=["pytest"],
)
