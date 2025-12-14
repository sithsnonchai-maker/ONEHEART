from oneheart import __version__, greet


def test_version_is_string():
    assert isinstance(__version__, str)


def test_greet_contains_name():
    assert "ONEHEART" in greet()
