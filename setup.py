#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of 19898.
# https://github.com/gr33ndata/19898

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Tarek Amr gr33ndata@yahoo.com


from setuptools import setup, find_packages
from 19898 import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='19898',
    version=__version__,
    description='CLI for downloading tweets',
    long_description='''
CLI for downloading tweets
''',
    keywords='twitter',
    author='Tarek Amr',
    author_email='gr33ndata@yahoo.com',
    url='https://github.com/gr33ndata/19898',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # '19898=19898.cli:main',
        ],
    },
)
