import pytest

from oneheart import __version__, greet


def test_version_is_string():
    assert isinstance(__version__, str)


def test_greet_default_contains_package_name():
    assert "ONEHEART" in greet()


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"
