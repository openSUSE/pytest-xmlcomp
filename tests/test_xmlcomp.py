# -*- coding: utf-8 -*-

from pytest_xmlcomp.plugin import stringifylist
from lxml import etree
import pytest


def test_pytest_collect_good_files(good_dir):
    result = good_dir.runpytest("-vs")
    assert result.ret == 0


def test_pytest_collect_bad_files(bad_dir):
    result = bad_dir.runpytest()
    assert result.ret == 1


@pytest.mark.parametrize("test_input, expected", [
        ([etree.Comment('foobar')], ['<!--foobar-->']),
        ([etree.ProcessingInstruction("instruction")], ['<?instruction?>']),
        ([etree.Element('foobar')], ['<foobar>']),
        (['simplestring'], ['simplestring']),
        ([etree._ElementUnicodeResult("foo")], ['foo'])
    ])
def test_stringifylist(test_input, expected):
    res = stringifylist(test_input)
    assert res == expected


def test_repr_failure_good_data(good_dir):
    result = good_dir.runpytest()
    assert result.ret == 0


def test_repr_failure_bad_data(bad_dir):
    result = bad_dir.runpytest()
    result.stdout.fnmatch_lines([
        "XPath execution failed"
    ])
    assert result.ret == 1


def test_pytest_xmlcomp_transform_xml(good_dir):
    good_dir.makeconftest("""
    def pytest_xmlcomp_transform_xml(xmlfile):
        from lxml import etree
        tree = etree.parse(source = str(xmlfile))
        return tree
    """)
    result = good_dir.runpytest("-sv")
    assert result.ret == 0


def test_XMLSyntaxError(synerror_dir):
    result = synerror_dir.runpytest("-sv")
    result.stderr.fnmatch_lines([
        "XML Syntax Error in file*"
        ])
    assert result.ret == 2
