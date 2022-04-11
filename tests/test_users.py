from fastapi.testclient import TestClient

from main import app
from tests.conftest import temp_database, drop_temp_database

client = TestClient(app)


@temp_database
def test_create_user():
    response = client.post("/security/register", json={
        "id": 1,
        "name": "test_user",
        "password": "test_password"}
    )
    assert response.status_code == 201
    assert response.json() == {'msg': 'User test_user created'}


@temp_database
def test_delete_user():
    response = client.delete("/users")
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
