import pytest
from py.path import local

pytest_plugins = 'pytester'

GOOD_DATA = local(__file__).dirpath("data/good/")
BAD_DATA = local(__file__).dirpath("data/bad/")
XML_SYNTAX_ERROR_DATA = local(__file__).dirpath("data/xml_syn_error")
JSON_SYNTAX_ERROR_DATA = local(__file__).dirpath("data/json_syn_error")


@pytest.fixture
def good_dir(testdir):
    gooddata_dir = testdir.tmpdir.mkdir("gooddata")
    for f in GOOD_DATA.listdir():
        f.copy(gooddata_dir)
    return testdir


@pytest.fixture
def bad_dir(testdir):
    baddata_dir = testdir.tmpdir.mkdir("baddata")
    for f in BAD_DATA.listdir():
        f.copy(baddata_dir)
    return testdir


@pytest.fixture
def xml_synerror_dir(testdir):
    xml_synerror_dir = testdir.tmpdir.mkdir("xml_syntax_error_data")
    for f in XML_SYNTAX_ERROR_DATA.listdir():
        f.copy(xml_synerror_dir)
    return testdir


@pytest.fixture
def json_synerror_dir(testdir):
    json_synerror_dir = testdir.tmpdir.mkdir("json_syntax_error_data")
    for f in JSON_SYNTAX_ERROR_DATA.listdir():
        f.copy(json_synerror_dir)
    return testdir
