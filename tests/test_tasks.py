from main import client
from tests.conftest import temp_database, user_authorization, drop_temp_database


@temp_database
def test_create_task():
    client.post("/tasks", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_task"})
    response = client.put("/tasks/1", headers=user_authorization(client), json={
        "name": "test_task",
        "contains": [
            {
                "name": "test_equipment",
                "id": 1,
                "contains": [
                    {
                        "name": "test_part",
                        "price": 0,
                        "id": 1,
                        'compatibility': 'test_equipment',
                        "contains": [
                            {
                                "name": "test_consumable",
                                "price": 0,
                                "id": 1,
                                'compatibility': 'test_part'
                            }
                        ]
                    }
                ]
            }
        ]})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "test_task",
        "contains": [
            {
                "name": "test_equipment",
                "id": 1,
                "contains": [
                    {
                        "name": "test_part",
                        "price": 0,
                        "id": 1,
                        'compatibility': 'test_equipment',
                        "contains": [
                            {
                                "name": "test_consumable",
                                "price": 0,
                                "id": 1,
                                'compatibility': 'test_part'
                            }
                        ]
                    }
                ]
            }
        ]
    }


@temp_database
def test_delete_task():
    response = client.delete("/tasks", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == []


def test_existing_temp_database():
    drop_temp_database()
