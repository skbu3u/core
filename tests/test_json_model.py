from fastapi.testclient import TestClient

from main import app
from tests.conftest import temp_database, drop_temp_database

client = TestClient(app)


@temp_database
def test_read_equipment_with_part_and_consumable():
    client.post("/equipments", json={
        "id": 1,
        "name": "test_equipment"})
    client.post("/parts", json={
        "id": 1,
        "name": "test_part",
        "price": 0,
        "compatibility": "test_equipment"})
    client.post("/consumables", json={
        "id": 1,
        "name": "test_consumable",
        "price": 0,
        "compatibility": "test_part"})
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


def test_existing_temp_database():
    drop_temp_database()
