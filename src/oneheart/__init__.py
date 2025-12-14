"""ONEHEART package — minimal core functionality."""

__all__ = ["__version__", "greet"]

__version__ = "0.1.0"


def greet(name: str = "ONEHEART") -> str:
    """Return a friendly greeting message.

    Args:
        name: Name to include in the greeting.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
