import pytest
from classes.SparePart import *


def test_init_spare_part():
    part = SparePart('Cartridge for drum unit')
    assert isinstance(part, SparePart)


def test_exception_if_spare_part_name_not_a_string():
    with pytest.raises(Exception) as ex:
        SparePart([])
    assert ex.type == ClassInitializationError


def test_add_part():
    part_1 = SparePart('Feed Drive for LaserJet 1020')
    part_2 = SparePart('Repair kit for LaserJet 1020')
    part_3 = SparePart('Fuser for LaserJet 1020')
    part_4 = SparePart('Main Motor for LaserJet 1020')
    part_1.add_part([part_2, part_3, part_4])
    for part in part_1.get_parts():
        assert isinstance(part, SparePart)
