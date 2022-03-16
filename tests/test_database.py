import pytest
from database.service import insert_values, select_values, delete_values, get_values


def test_database_values():
    insert_values('Cartridge', 50)
    assert select_values(part_id=1) == (1, 'Cartridge', 50)
    delete_values('Cartridge')
