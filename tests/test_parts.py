import pytest
from fastapi.testclient import TestClient

from main import app
from src.database.models import PartModel
from tests.conftest import temp_database, drop_temp_database, user_authorization

client = TestClient(app)


def test_init_part():
    part = PartModel(name='Repair kit for LaserJet 1020', price=40)
    assert isinstance(part, PartModel)


def test_exception_if_part_name_not_a_string():
    with pytest.raises(Exception) as ex:
        PartModel([])
    assert ex.type == TypeError


@temp_database
def test_create_part():
    response = client.post("/parts", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_part",
        "price": 0,
        "compatibility": "test_equipment"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "test_part",
        "contains": []
    }


@temp_database
def test_delete_part():
    response = client.delete("/parts", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
