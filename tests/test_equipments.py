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
        "parts": []
    }


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
        "parts": []
    }


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
def test_read_equipment_with_part_and_consumable():
    response = client.get("/equipments")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "test_equipment",
            "id": 1,
            "parts": [
                {
                    "name": "test_part",
                    "price": 0,
                    "id": 1,
                    "consumables": [
                        {
                            "name": "test_consumable",
                            "price": 0,
                            "id": 1
                        }
                    ]
                }
            ]
        }
    ]


@temp_database
def test_delete_equipment():
    response = client.delete("/equipments")
    assert response.status_code == 200
    assert response.json() == []


@temp_database
def test_delete_part():
    response = client.delete("/parts")
    assert response.status_code == 200
    assert response.json() == []


@temp_database
def test_delete_consumable():
    response = client.delete("/consumables")
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
