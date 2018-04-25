# -*- coding: utf-8 -*-

__version__ = "0.2.0"

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('xmlcomp')
    group.addoption(
        '--datadir',
        action='store',
        dest='datadir',
        default='data',
        help='Give the directory containing the XML files.'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.datadir
