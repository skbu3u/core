import pytest
from main import greet

entry = 123


def test_is_str():
    assert isinstance(greet(entry), str)
