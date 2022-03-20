import pytest
from classes.Report import Report
from classes.Equipment import Equipment
from exceptions.ClassInitializationError import ClassInitializationError


def test_init_report():
    model = Equipment('HP LaserJet 1020')
    report = Report(model)
    assert isinstance(report.info, dict)


def test_exception_if_report_info_not_a_equipment():
    with pytest.raises(Exception) as ex:
        Report([])
    assert ex.type == ClassInitializationError
