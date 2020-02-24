#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os.path import (abspath, dirname, join)
from subprocess import call

from setuptools import (Command, find_packages, setup)

from ImpSort.version import (__version__, __author__, __email__, __license__)

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class RunTests(Command):
    """Run all tests."""

    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        cwd = join(this_dir, 'tests')
        err_no = call(['py.test', '--cov=ImpSort', '--cov-report=term-missing'], cwd=cwd)
        raise SystemExit(err_no)


setup(
    name='ImpSort',
    version=__version__,
    description='A python library for interacting with some very terrible sorting algorithms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/thedeltaflyer/ImpSort',
    author=__author__,
    author_email=__email__,
    license=__license__,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='sorting bogo rand_swap',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    cmdclass={'test': RunTests},
)
