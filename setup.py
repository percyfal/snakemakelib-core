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
    'pytest',
    'pytest-cov',
    'pytest-mock',
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
# https://pytest.org/latest/goodpractises.html#integrating-with-distutils-python-setup-py-test
from distutils.core import setup, Command
# you can also import from setuptools

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

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
        'snakemakelib.bio',
        'snakemakelib.bio.ngs',
        'snakemakelib.bio.ngs.rnaseq',
        'snakemakelib.db',
        'snakemakelib.graphics',
        'snakemakelib.odo',
        'snakemakelib.plot',
        'snakemakelib.plot.bokeh',
        'snakemakelib.report',
        'snakemakelib.sample',
        'snakemakelib.sample.organization',
        'snakemakelib.tools',
    ],
    package_data={'snakemakelib': package_data},
    install_requires=REQUIRES,
)
