import pytest
from classes.SparePart import *


def test_init_spare_part():
    part = SparePart('Drumunit for LaserJet 1020')
    assert isinstance(part, SparePart)


def test_exception_if_spare_part_name_not_a_string():
    with pytest.raises(Exception) as ex:
        SparePart([])
    assert ex.type == ClassInitializationError


def test_add_part():
    part_1 = SparePart('Drumunit for LaserJet 1020')
    part_2 = SparePart('Cartridge for drumunit')
    part_1.add_part([part_2])
    # assert isinstance(__parts, list)


def test_to_json():
    part = SparePart('Drumunit for LaserJet 1020')
    # print(part.to_json())
    assert part.to_json() == '{"name": "Drumunit for LaserJet 1020", "parts": []}'
