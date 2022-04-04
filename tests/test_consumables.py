from fastapi.testclient import TestClient

from main import app
from tests.conftest import temp_database, drop_temp_database

client = TestClient(app)


@temp_database
def test_create_consumable():
    response = client.post("/consumables", json={
        "id": 1,
        "name": "test_consumable",
        "price": 0,
        "compatibility": "test_part"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "test_consumable",
        "price": 0,
        "consumables": []
    }


@temp_database
def test_delete_consumable():
    response = client.delete("/consumables")
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
