import pytest
from models import *


def test_is_printer():
    model = Printer()
    assert model.printer


def test_is_scaner():
    model = Scaner()
    assert model.scaner


def test_is_xerox():
    model = Xerox()
    assert model.xerox
