#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


def requires(filename):
    """Returns a list of all pip requirements, but ignores empty lines or
       lines starting with '#' or '-'
    :param filename: the Pip requirement file (usually 'requirements.txt')
    :return: list of modules
    :rtype: list
    """
    modules = []
    with open(filename, 'r') as pipreq:
        for line in pipreq:
            line = line.strip()
            if not line or line[0] in ('-', '#'):
                continue
            modules.append(line)
    return modules


setup(
    name='pytest-xmlcomp',
    version='0.3.0',
    author='Fabian Baumanis',
    author_email='fabian.baumanis@suse.com',
    maintainer='Fabian Baumanis',
    maintainer_email='fabian.baumanis@suse.com',
    license='GNU GPL v3.0',
    url='https://github.com/openSUSE/pytest-xmlcomp',
    description='A simple plugin comparing XML files.',
    long_description=read('README.rst'),
    packages=find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=requires(os.path.abspath("requirements.pip")),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    entry_points={
        'pytest11': [
                  'pytest-xmlcomp = pytest_xmlcomp.plugin',
        ],
    },
)
