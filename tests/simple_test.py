import pytest
from main import greet

entry = 'Hello'


def test_is_str():
    assert isinstance(greet(entry), str)
