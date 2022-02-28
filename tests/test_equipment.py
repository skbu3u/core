import pytest
from classes.Equipment import *
from classes.SparePart import *


def test_init_spare_part():
    part = Equipment('HP LaserJet 1020')
    assert isinstance(part, Equipment)


def test_exception_if_equipment_name_not_a_string():
    with pytest.raises(Exception) as ex:
        Equipment([])
    assert ex.type == ClassInitializationError


def test_add_part():
    part_1 = Equipment('HP LaserJet 1020')
    part_2 = Equipment('Repair kit for LaserJet 1020')
    part_3 = Equipment('Fuser for LaserJet 1020')
    part_4 = Equipment('Main Motor for LaserJet 1020')
    part_1.add_part([part_2, part_3, part_4])
    for part in part_1.get_parts_info():
        assert isinstance(part, Equipment)