# -*- coding: utf-8 -*-


def test_bar_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_sth(bar):
            assert bar == "europython2015"
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--datadir=europython2015',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_sth PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_xmljsonfiles_fixture(testdir):
    from py.path import local
    p = local(__file__).dirpath("data")
    targetdata = testdir.tmpdir.mkdir("data")
    for f in p.listdir():
        f.copy(targetdata)
    testdir.makepyfile("""
        def test_xmljsonfiles_fixture(xmljsonfiles):
            assert xmljsonfiles
        """)
    result = testdir.runpytest('--datadir=data', '-v')
    result.stdout.fnmatch_lines([
        '*::test_xmljsonfiles_fixture PASSED*',
    ])
    assert result.ret == 0


def test_xmljsonfiles_noXML_fixture(testdir):
    from py.path import local
    p = local(__file__).dirpath("data")
    targetdata = testdir.tmpdir.mkdir("data")
    for f in p.listdir():
        if f.ext == ".xml":
            continue
        f.copy(targetdata)
    testdir.makepyfile("""
        def test_xmljsonfiles_fixture(xmljsonfiles):
            assert xmljsonfiles
        """)
    result = testdir.runpytest('--datadir=data', '-v')
    result.stdout.fnmatch_lines([
        '*::test_xmljsonfiles_fixture FAILED*',
    ])
    assert result.ret == 1


def test_xmljsonfiles__noJSON_fixture(testdir):
    from py.path import local
    p = local(__file__).dirpath("data")
    targetdata = testdir.tmpdir.mkdir("data")
    for f in p.listdir():
        if f.ext == ".json":
            continue
        f.copy(targetdata)
    testdir.makepyfile("""
        def test_xmljsonfiles_fixture(xmljsonfiles):
            assert xmljsonfiles
        """)
    result = testdir.runpytest('--datadir=data', '-v')
    assert result.ret == 1


def test_compare_xml_with_json(testdir):
    from py.path import local
    p = local(__file__).dirpath("data")
    targetdata = testdir.tmpdir.mkdir("data")
    for f in p.listdir():
        f.copy(targetdata)
    testdir.makepyfile("""
        import pytest_xmlcomp as py_x
        def test_compare_xml_with_json(xmljsonfiles):
            assert py_x.compare_xml_with_json(xmljsonfiles)
        """)
    result = testdir.runpytest('--datadir=data', '-v')
    result.stdout.fnmatch_lines([
        '*::test_compare_xml_with_json PASSED*',
    ])
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'xmlcomp:',
        '*--datadir=DATADIR*Give the directory containing the XML files.',
    ])


def test_hello_ini_setting(testdir):
    testdir.makeini("""
        [pytest]
        HELLO = world
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.fixture
        def hello(request):
            return request.config.getini('HELLO')

        def test_hello_world(hello):
            assert hello == 'world'
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_hello_world PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
