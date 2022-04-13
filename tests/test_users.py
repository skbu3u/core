from fastapi.testclient import TestClient

from main import app
from tests.conftest import temp_database, drop_temp_database, user_authorization

client = TestClient(app)


@temp_database
def test_create_user():
    response = client.post("/security/register", json={
        "id": 1,
        "name": "test_user",
        "password": "test_password"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data[1] == {'msg': 'User test_user created'}


@temp_database
def test_delete_user():
    response = client.delete("/users", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
