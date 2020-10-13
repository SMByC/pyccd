"""pyccd is an implementation of the Continuous Change Detection
algorithm. This is designed for inclusion into the LCMAP project.

Principal Algorithm investigator:

Zhe Zhu
Assistant Professor,
Department of Geosciences,
Texas Tech University, TX, USA
"""

from setuptools import setup
from os import path
import io

here = path.abspath(path.dirname(__file__))


# bring in __version__ and __name from version.py for install.
with open(path.join(here, 'ccd', 'version.py')) as h:
    exec(h.read())

def readme():
    with open('README.md') as f:
        return f.read()

setup(

    # __name is defined in version.py
    name=__name,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html

    # __version is defined in version.py
    version=__version,

    description='Python implementation of Continuous Change Detection',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://code.usgs.gov/lcmap/pyccd',
    maintainer='Kelcy Smith',
    maintainer_email='klsmith@contractor.usgs.gov',
    license='Public Domain',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='python change detection',

    packages=['ccd', 'ccd.models'],

    install_requires=['numpy>=1.10.0',
                      'scipy>=0.18.1',
                      'scikit-learn>=0.18'],
    
    extras_require={
        'test': ['aniso8601>=1.1.0',
                 'flake8>=3.0.4',
                 'coverage>=4.2',
                 'pytest>=3.0.2',
                 'pytest-profiling>=1.1.1',
                 'gprof2dot>=2015.12.1',
                 'pytest-watch>=4.1.0'],
        'dev': ['jupyter',
                'line_profiler'],
        'docs': ['sphinx',
                 'sphinx-autobuild',
                 'sphinx_rtd_theme'],
        'deploy': ['twine']
    },

    setup_requires=['pytest-runner', 'pip'],
    tests_require=['pytest>=3.0.2'],
)
