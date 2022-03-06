import pytest
from classes.Report import *


def test_init_report():
    model = Equipment('HP LaserJet 1020')
    report = Report(model)
    assert isinstance(report.info, dict)
