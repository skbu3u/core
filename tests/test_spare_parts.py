import pytest

from src.classes.SparePart import SparePart
from src.exceptions import ClassInitializationError


def test_init_spare_part():
    part = SparePart('Cartridge for drum unit', 50)
    assert isinstance(part, SparePart)


def test_exception_if_spare_part_name_not_a_string():
    with pytest.raises(Exception) as ex:
        SparePart([], 50)
    assert ex.type == ClassInitializationError
