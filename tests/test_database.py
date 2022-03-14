import pytest
from database.service import insert_values, select_values, delete_values, get_values


def test_database_values():
    insert_values('Cartridge', 50)
    # delete_values('Cartridge')
    assert get_values().type == sqlalchemy
