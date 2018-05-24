import pytest
from py.path import local

pytest_plugins = 'pytester'

GOOD_DATA = local(__file__).dirpath("data/good/")
BAD_DATA = local(__file__).dirpath("data/bad/")


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
