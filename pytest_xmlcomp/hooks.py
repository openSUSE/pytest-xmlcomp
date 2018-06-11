from lxml import etree
import sys

"""Custom hooks for pytest-xmlcomp"""


def pytest_xmlcomp_transform_xml(xmlfile):
    """
    Hook for transforming XML

    :param xmlfile: Input XML file which will be modified
    :type xmlfile: str | :py:class:`py.path.local`
    :returns: The modified XML file.
    """
    try:
        tree = etree.parse(source=str(xmlfile))
    except etree.XMLSyntaxError as error:
        print("XML Syntax Error in file %s:\n%s" % (xmlfile, error),
              file=sys.stderr)
        return None
    # tree modification here
    return tree
