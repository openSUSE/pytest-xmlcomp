# -*- coding: utf-8 -*-

from py.path import local
from pytest_xmlcomp import stringifylist
from pytest_xmlcomp import XMLJSONFile
from lxml import etree
import pytest

GOOD_DATA = local(__file__).dirpath("data/good")
BAD_DATA = local(__file__).dirpath("data/bad")


def test_pytest_collect_good_files(testdir):
    targetdata = testdir.tmpdir.mkdir("gooddata")
    for f in GOOD_DATA.listdir():
        f.copy(targetdata)
    result = testdir.runpytest()
    assert result.ret == 0

def test_pytest_collect_bad_files(testdir):
    targetdata = testdir.tmpdir.mkdir("baddata")
    for f in BAD_DATA.listdir():
        f.copy(targetdata)
    result = testdir.runpytest()
    result.stdout.fnmatch_lines([
        "False <class 'list'> [] ['<baz>']"
    ])
    assert result.ret == 1

@pytest.mark.parametrize("test_input, expected", [
        ([etree.Comment('foobar')], ['<!--foobar-->']),
        ([etree.ProcessingInstruction("instruction")], ['<?instruction?>']),
        ([etree.Element('foobar')], ['<foobar>']),
        (['simplestring'], ['simplestring'])
    ])
def test_stringifylist(test_input, expected):
    res = stringifylist(test_input)
    assert res == expected

def test_XPathItem_init(testdir):
    targetdata = testdir.tmpdir.mkdir("reprfailure_test")
    for f in GOOD_DATA.listdir():
        f.copy(targetdata)
    result = testdir.runpytest()
    assert result.ret == 0


def test_repr_failure_good_data(testdir):
    targetdata = testdir.tmpdir.mkdir("reprfailure_test")
    for f in GOOD_DATA.listdir():
        f.copy(targetdata)
    result = testdir.runpytest()
    assert result.ret == 0

def test_repr_failure_bad_data(testdir):
    targetdata = testdir.tmpdir.mkdir("reprfailure_test")
    for f in BAD_DATA.listdir():
        f.copy(targetdata)
    result = testdir.runpytest()
    assert result.ret == 1


