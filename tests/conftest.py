import pytest
from py.path import local

pytest_plugins = 'pytester'

GOOD_DATA = local(__file__).dirpath("data/good/")
GOOD_DATA_NSP = local(__file__).dirpath("data/good_namesp/")
BAD_DATA = local(__file__).dirpath("data/bad/")
BAD_DATA_NSP = local(__file__).dirpath("data/bad_namesp/")
XML_SYN_ERROR_DATA = local(__file__).dirpath("data/xml_syn_error")
XML_SYN_ERROR_NSP_DATA = local(__file__).dirpath("data/xml_syn_error_nsp")
JSON_SYN_ERROR_DATA = local(__file__).dirpath("data/json_syn_error")
JSON_SYN_ERROR_NSP_DATA = local(__file__).dirpath("data/json_syn_error_nsp")


@pytest.fixture
def good_dir(testdir):
    gooddata_dir = testdir.tmpdir.mkdir("gooddata")
    for f in GOOD_DATA.listdir():
        f.copy(gooddata_dir)
    return testdir


@pytest.fixture
def good_namespaces_dir(testdir):
    good_namespaces_dir = testdir.tmpdir.mkdir("goodnamespace")
    for f in GOOD_DATA_NSP.listdir():
        f.copy(good_namespaces_dir)
    return testdir


@pytest.fixture
def bad_dir(testdir):
    baddata_dir = testdir.tmpdir.mkdir("baddata")
    for f in BAD_DATA.listdir():
        f.copy(baddata_dir)
    return testdir


@pytest.fixture
def bad_namespaces_dir(testdir):
    bad_namespaces_dir = testdir.tmpdir.mkdir("badnamespace")
    for f in BAD_DATA_NSP.listdir():
        f.copy(bad_namespaces_dir)
    return testdir


@pytest.fixture
def xml_synerror_dir(testdir):
    xml_synerror_dir = testdir.tmpdir.mkdir("xml_syntax_error_data")
    for f in XML_SYN_ERROR_DATA.listdir():
        f.copy(xml_synerror_dir)
    return testdir


@pytest.fixture
def json_synerror_dir(testdir):
    json_synerror_dir = testdir.tmpdir.mkdir("json_syntax_error_data")
    for f in JSON_SYN_ERROR_DATA.listdir():
        f.copy(json_synerror_dir)
    return testdir


@pytest.fixture
def json_synerror_namespaces_dir(testdir):
    json_synerror_nsp_dir = testdir.tmpdir.mkdir("json_syntax_error_nsp_data")
    for f in JSON_SYN_ERROR_NSP_DATA.listdir():
        f.copy(json_synerror_nsp_dir)
    return testdir


@pytest.fixture
def xml_synerror_nsp_dir(testdir):
    xml_synerror_nsp_dir = testdir.tmpdir.mkdir("xml_syntax_error_nsp_data")
    for f in XML_SYN_ERROR_DATA.listdir():
        f.copy(xml_synerror_nsp_dir)
    return testdir
