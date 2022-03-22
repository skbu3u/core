import pytest
from src.classes.Equipment import Equipment
from src.classes.SparePart import SparePart
from src.exceptions.ClassInitializationError import ClassInitializationError


def test_init_spare_part():
    part = Equipment('HP LaserJet 1020')
    assert isinstance(part, Equipment)


def test_exception_if_equipment_name_not_a_string():
    with pytest.raises(Exception) as ex:
        Equipment([])
    assert ex.type == ClassInitializationError


def test_add_parts_to_model():
    model = Equipment('HP LaserJet 1020')
    part_1 = SparePart('Feed Drive for LaserJet 1020', 20)
    part_2 = SparePart('Repair kit for LaserJet 1020', 10)
    part_3 = SparePart('Fuser for LaserJet 1020', 80)
    part_4 = SparePart('Main Motor for LaserJet 1020', 40)
    model.add_part_list([part_1, part_2, part_3, part_4])
    assert isinstance(model.get_parts, dict)
