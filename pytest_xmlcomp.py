# -*- coding: utf-8 -*-

__version__ = "0.2.0"

import pytest
from py.path import local
import json
from lxml import etree

def pytest_collect_file(parent, path):
    jsonfile = path.new(ext = ".json")
    if path.ext == ".xml" and jsonfile.exists():
        print("XML file %s and JSON file %s found" % (path, jsonfile))
        return XMLJSONFile(path, parent)

class XMLJSONFile(pytest.File):
    def collect(self):
        from lxml import etree
        import json
        try:
            tree = etree.parse(self.fspath.open())
        except etree.XMLSyntaxError:
            print("XML Syntax Error in file %s" % self.fspath)
            return False
        root = tree.getroot()
        jsonfile = self.fspath.new(ext = '.json')
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
    
    def runtest(self):
        res = self.tree.xpath(self.xpath)
        print (bool(res))
        print (type(res))
        if isinstance(res, (float, str)):
            if res != self.expresult:
                ValueError("XPath %s is not in XML file %s !" % (self.xpath, self.tree.docinfo.URL))
        elif isinstance(res, list):
            if bool(res) == bool(self.expresult):
                ValueError("XPath %s is not in XML file %s !" % (self.xpath, self.tree.docinfo.URL))
        return True
