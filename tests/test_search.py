from main import client
from tests.conftest import temp_database, drop_temp_database, user_authorization


@temp_database
def test_search_users():
    response = client.get("/search/users/test", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "test_user"
    }]


def test_search_equipments():
    response = client.get("/search/equipments/test", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == {'detail': 'No matches found'}


def test_existing_temp_database():
    drop_temp_database()
