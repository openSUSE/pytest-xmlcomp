# -*- coding: utf-8 -*-

__version__ = "0.3.0"

import pytest
from lxml import etree
from pytest_xmlcomp import hooks
import sys


def pytest_addoption(parser):
    """
    Add options to pytest-xmlcomp

    :param parser: the parser object
    :type parser: :class:`_pytest.config.Parser`
    """
    group = parser.getgroup('xmlcomp')
    group.addoption(
            '--datadir',
            action='store',
            dest='datadir',
            default='tests/data',
            help='Give the directory containing the XML files.')


def pytest_addhooks(pluginmanager):
    """
    Add custom hook from hooks.py and register it.

    :param pluginmanager: The Plugin manager from pytest.
    :class:`_pytest.config.PytestPluginManager`
    """
    pluginmanager.add_hookspecs(hooks)
    pluginmanager.register(hooks, "xmlcomp")


def pytest_collect_file(parent, path):
    """
    Collects all XML and corresponding JSON files and returns them.

    :param parent:
    :type parent: :class:`_pytest.main.Session'
    :param path: the path to collect
    :type path: :class:`py._path.local.LocalPath`
    :return: a XML and JSON file pair
    :rtype: :class:`XMLJSONFile`
    """
    jsonfile = path.new(ext=".json")
    if path.ext == ".xml" and jsonfile.exists():
        print("XML file %s and JSON file %s found" % (path, jsonfile))
        return XMLJSONFile(path, parent)


def stringifylist(res):
        """
        Converts the result of the XPath comparison into a string.
        :param res: Result of XPath comparison
        :returns result: list with the string/object
        """
        result = []
        for obj in res:
            if isinstance(obj, (etree._Comment, etree._ProcessingInstruction)):
                result.append(str(obj))
            elif isinstance(obj, etree._Element):
                result.append("<%s>" % obj.tag)
            elif isinstance(obj, str):
                result.append(obj)
        return result


class XMLJSONFile(pytest.File):
    def collect(self):
        """
        Modify the XML files via a custom hook and parse the JSON.
        Returns: It returns XPath items which are found in the JSON file.
        """
        import json
        xmlfile = self.fspath
        print(self.fspath)
        pm = self.config.pluginmanager
        tree = pm.hook.pytest_xmlcomp_transform_xml(xmlfile=str(xmlfile))
        if tree is None:
            return
        jsonfile = self.fspath.new(ext='.json')
        try:
            jsondata = json.load(open(str(jsonfile)))
        except json.decoder.JSONDecodeError as error:
            print("JSON Syntax Error in file %s:\n%s" % (jsonfile, error),
                  file=sys.stderr)
            return
        for xpath, expresult in jsondata:
            yield XPathItem(xpath, self, expresult, tree)


class XPathItem(pytest.Item):
    def __init__(self, xpath, parent, expresult, tree):
        """
        Initializes the XPath item.
        :param xpath: the xpath item
        :param parent:
        :param expresult: the result which will be expected.
        :param tree: the tree of the XML file
        :type xpath: xpath object
        :type parent: :class:`_pytest.main.Session'
        :type expresult: JSON object
        :type tree: class lxml.ElementTree
        """
        super().__init__(xpath, parent)
        self.expresult = expresult
        self.xpath = self.name
        self.tree = tree[0]
        self.root = tree[0].getroot()
        print(self.root)

    def runtest(self):
        """
        Apply an XPath to the modified XML file and check the result.
        :raises XPathError: result of XPath doesn't match with modified XML
        """
        res = self.tree.xpath(self.xpath)
        if isinstance(res, list):
            res = stringifylist(res)
            if res != self.expresult:
                raise XPathError(
                    self.xpath, res, self.expresult, self.tree.docinfo.URL
                )
        return True

    def repr_failure(self, excinfo):
        """
        Called when self.runtest() raises an exception.
        :param excinfo: the Information about the exception
        :type excinfo: a tuple with exception informations
        """
        if isinstance(excinfo.value, XPathError):
            return "\n".join([
                "XPath execution failed",
                "           file: %r" % excinfo.value.args[-1],
                "   XPath failed: %r:" % excinfo.value.args[0],
                "         result: %s" % excinfo.value.args[1],
                "       expected: %s" % excinfo.value.args[2],
            ])

    def reportinfo(self):
        """
        Returns an error for the failed XPath.
        """
        return self.fspath, 0, "XPath: %s" % self.name


class XPathError(Exception):
    """XPath Evaluation Error"""
    pass
