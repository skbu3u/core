from main import client
from src.database.models import EquipmentModel, PartModel, ConsumableModel
from tests.conftest import temp_database, drop_temp_database, user_authorization


def test_add_parts_and_consumable_to_equipment():
    equipment = EquipmentModel(name='HP LaserJet 1020')
    part = PartModel(name='Repair kit for LaserJet 1020', price=40)
    consumable = ConsumableModel(name='Feed Drive', price=15)
    equipment.contains.append(part)
    part.contains.append(consumable)
    assert isinstance(equipment, EquipmentModel)
    for item in equipment.contains:
        assert isinstance(item, PartModel)
    for item in part.contains:
        assert isinstance(item, ConsumableModel)


@temp_database
def test_read_equipment_with_part_and_consumable():
    client.post("/equipments", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_equipment"})
    client.post("/parts", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_part",
        "price": 0,
        "compatibility": "test_equipment"})
    client.post("/consumables", headers=user_authorization(client), json={
        "id": 1,
        "name": "test_consumable",
        "price": 0,
        "compatibility": "test_part"})
    response = client.get("/equipments", headers=user_authorization(client))
    assert response.status_code == 200
    assert response.json() == [
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


def test_existing_temp_database():
    drop_temp_database()
