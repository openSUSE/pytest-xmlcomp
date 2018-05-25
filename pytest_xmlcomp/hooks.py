"""Custom hooks for pytest-xmlcomp"""


def pytest_transform_xml(xmlfile):
    """
    Hook for transforming XML
    :param xmlfile: Input XML file which will be modified
    :returns: The modified XML file.
    """

    print("Given XML file: %s", xmlfile)
    return xmlfile
