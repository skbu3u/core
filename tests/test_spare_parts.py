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
    part = SparePart('Feed Drive for LaserJet 1020')
    parts_list = ['Repair kit for LaserJet 1020', 'Fuser for LaserJet 1020', 'Main Motor for LaserJet 1020']
    part.add_part(parts_list)
    assert isinstance(part.get_parts_info(), list)


def test_to_json():
    part = SparePart('Drum Unit for LaserJet 1020')
    assert part.to_json() == '{"name": "Drum Unit for LaserJet 1020", "parts": ["Drum Unit for LaserJet 1020"]}'
