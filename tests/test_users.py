from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/security/register", json={
        "id": 1,
        "name": "test_user",
        "email": "test@mail.com",
        "password": "test_password"}
    )
    assert response.status_code == 201
    assert response.json() == {'msg': 'User test_user created'}


def test_delete_user():
    response = client.delete("/users")
    assert response.status_code == 200
    assert response.json() == []
