import pytest

from main import client
from src.database.models import EquipmentModel
from tests.conftest import temp_database, drop_temp_database, user_authorization


def test_init_equipment():
    equipment = EquipmentModel(name='HP LaserJet 1020')
    assert isinstance(equipment, EquipmentModel)


def test_exception_if_equipment_name_not_a_string():
    with pytest.raises(Exception) as ex:
        EquipmentModel([])
    assert ex.type == TypeError


@temp_database
def test_create_equipment():
    response = client.post("/equipments", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_equipment"})
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "test_equipment",
        "contains": []
    }


@temp_database
def test_delete_equipment():
    response = client.delete("/equipments", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
