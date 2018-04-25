# -*- coding: utf-8 -*-

__version__ = "0.2.0"

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('xmlcomp')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2018',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo
