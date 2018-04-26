# -*- coding: utf-8 -*-

__version__ = "0.2.0"

import pytest
from py.path import local

def pytest_addoption(parser):
    group = parser.getgroup('xmlcomp')
    group.addoption(
        '--datadir',
        action='store',
        dest='datadir',
        default='tests/data',
        help='Give the directory containing the XML files.')

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.datadir

@pytest.fixture
def check_for_files(request):
    result = []
    # create Pathlib object for the given data directory
    p = local(request.config.option.datadir)
    # create filter for listdir function
    def xml_filter(x):
        if x.ext == ".xml":
            return x
    #iterate over the file list
    for f in p.listdir(fil=xml_filter):
        out = f.new(ext = ".out")
        if not out.exists():
            print("No output files found")
            continue
        err = f.new(ext = ".err")
        if not err.exists():
            result.append((f,out,None))
        else:
            result.append((f,out,err))
    return result
