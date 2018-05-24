# -*- coding: utf-8 -*-

__version__ = "0.3.0"

import pytest
from lxml import etree
from pytest_xmlcomp import hooks


def pytest_addoption(parser):
    group = parser.getgroup('xmlcomp')
    group.addoption(
            '--datadir',
            action='store',
            dest='datadir',
            default='tests/data',
            help='Give the directory containing the XML files.')


def pytest_addhooks(pluginmanager):
    pluginmanager.add_hookspecs(hooks)
    pluginmanager.register(hooks, "xmlcomp")


def pytest_collect_file(parent, path):
    jsonfile = path.new(ext=".json")
    if path.ext == ".xml" and jsonfile.exists():
        print("XML file %s and JSON file %s found" % (path, jsonfile))
        return XMLJSONFile(path, parent)


def stringifylist(res):
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
        from lxml import etree
        import json
        originalxmlfile = self.fspath
        pm = self.config.pluginmanager
        modifiedxmlfile = pm.hook.pytest_transform_xml(xmlfile=originalxmlfile)
        try:
            tree = etree.parse(str(modifiedxmlfile[0]))
        except etree.XMLSyntaxError:
            print("XML Syntax Error in file %s" % self.fspath)
            return False
        jsonfile = self.fspath.new(ext='.json')
        jsondata = json.load(open(str(jsonfile)))
        for xpath, expresult in jsondata:
            yield XPathItem(xpath, self, expresult, tree)


class XPathItem(pytest.Item):
    def __init__(self, xpath, parent, expresult, tree):
        super().__init__(xpath, parent)
        self.expresult = expresult
        self.xpath = self.name
        self.tree = tree
        self.root = tree.getroot()
        print(self.root)

    def runtest(self):
        res = self.tree.xpath(self.xpath)
        print(bool(res), type(res), res, self.expresult)
        if isinstance(res, list):
            res = stringifylist(res)
            if res != self.expresult:
                raise XPathError(
                    self.xpath, res, self.expresult, self.tree.docinfo.URL
                )
        return True

    def repr_failure(self, excinfo):
        """ called when self.runtest() raises an exception. """
        if isinstance(excinfo.value, XPathError):
            return "\n".join([
                "XPath execution failed",
                "           file: %r" % excinfo.value.args[-1],
                "   XPath failed: %r:" % excinfo.value.args[0],
                "         result: %s" % excinfo.value.args[1],
                "       expected: %s" % excinfo.value.args[2],
            ])

    def reportinfo(self):
        return self.fspath, 0, "XPath: %s" % self.name


class XPathError(Exception):
    """XPath Evaluation Error"""
    pass
