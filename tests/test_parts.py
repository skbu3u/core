from fastapi.testclient import TestClient

from main import app
from tests.conftest import temp_database, drop_temp_database

client = TestClient(app)


@temp_database
def test_create_part():
    response = client.post("/parts", json={
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
    response = client.delete("/parts")
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
