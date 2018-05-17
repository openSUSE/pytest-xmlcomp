# -*- coding: utf-8 -*-

from py.path import local

DATADIR = local(__file__).dirpath("data")

def test_testdir(testdir):
    targetdata = testdir.tmpdir.mkdir("data")
    for f in DATADIR.listdir():
        f.copy(targetdata)
    testdir.makepyfile("""
        def test_foo():
            assert True
        """)
    result = testdir.runpytest()
    assert result.ret == 0

