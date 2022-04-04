from fastapi.testclient import TestClient

from main import app
from tests.conftest import temp_database, drop_temp_database

client = TestClient(app)


@temp_database
def test_create_equipment():
    response = client.post("/equipments", json={
        "id": 1,
        "name": "test_equipment"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "test_equipment",
        "contains": []
    }


@temp_database
def test_delete_equipment():
    response = client.delete("/equipments")
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
