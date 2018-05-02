# -*- coding: utf-8 -*-

__version__ = "0.2.0"

import pytest
from py.path import local
import json
from lxml import etree


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
    # iterate over the file list

    def xml_filter(x):
        if x.ext == ".xml":
            return x
    for f in p.listdir(fil=xml_filter):
        json = f.new(ext=".json")
        if not json.exists():
            raise ValueError ("JSON file not found!")
        result.append((f, json))
    return result


@pytest.fixture
def compare_xml_with_json(request):
    # create Pathlib object for the given data directory
    p = local(request.config.option.datadir)
    # iterate over Pathlib object

    def xml_filter(x):
        if x.ext == ".xml":
            return x
    for f in p.listdir(fil=xml_filter):
        root = etree.parse(str(f))
        j = f.new(ext=".json")
        jsondata = json.load(open(j))
    for xpath, expresult in jsondata:
        res = root.xpath(xpath)
        if not res:
            raise ValueError("XPath is not in XML file!")
    return True
