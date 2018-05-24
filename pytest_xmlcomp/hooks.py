"""Custom hooks for pytest-xmlcomp"""


def pytest_transform_xml(xmlfile):
    """Hook for transforming XML"""
    print("Given XML file: %s", xmlfile)
    return xmlfile
