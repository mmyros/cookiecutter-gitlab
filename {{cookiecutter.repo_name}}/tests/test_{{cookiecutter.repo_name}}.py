# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.credits }}

import pkg_resources

import pytest

try:
    from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}
except pkg_resources.DistributionNotFound:
    raise ImportError("did you run 'pip install -e .' for your project")


def test_import():
    {{ cookiecutter.repo_name }}.say_hello()


"""
you are looking for setup / teardown methods? py.test has fixtures:
    http://doc.pytest.org/en/latest/fixture.html
you find examples below
"""


@pytest.yield_fixture
def one():
    print("setup")
    yield 1
    print("teardown")


def test_something(one):
    assert one == 1
