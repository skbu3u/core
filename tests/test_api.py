from main import client


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hi from backend!'}
