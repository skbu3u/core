import pytest

from main import client
from src.database.models import ConsumableModel
from tests.conftest import temp_database, drop_temp_database, user_authorization


def test_init_consumable():
    consumable = ConsumableModel(name='Feed Drive', price=15)
    assert isinstance(consumable, ConsumableModel)


def test_exception_if_consumable_name_not_a_string():
    with pytest.raises(Exception) as ex:
        ConsumableModel([])
    assert ex.type == TypeError


@temp_database
def test_create_consumable():
    response = client.post("/consumables", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_consumable",
        "price": 0,
        "compatibility": "test_part"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "test_consumable",
        "price": 0,
        'compatibility': 'test_part',
        "contains": []
    }


@temp_database
def test_delete_consumable():
    response = client.delete("/consumables", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
