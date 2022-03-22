from fastapi_crudrouter import SQLAlchemyCRUDRouter

from src.api.schemas.consumables import Consumable, ConsumableCreate
from src.api.schemas.equipments import Equipment, EquipmentCreate
from src.api.schemas.parts import Part, PartCreate
from src.api.schemas.users import User, UserCreate
from src.database.models.consumables import ConsumableModel
from src.database.models.equipments import EquipmentModel
from src.database.models.parts import PartModel
from src.database.models.users import UserModel
from src.database.sql import get_db


def add_route(schema, create_schema, db_model, prefix, create_route=True):
    route = SQLAlchemyCRUDRouter(
        schema=schema,
        create_schema=create_schema,
        db_model=db_model,
        db=get_db,
        prefix=prefix,
        create_route=create_route
    )
    return route


users = add_route(User, UserCreate, UserModel, 'users', False)
equipments = add_route(Equipment, EquipmentCreate, EquipmentModel, 'equipments')
parts = add_route(Part, PartCreate, PartModel, 'parts')
consumables = add_route(Consumable, ConsumableCreate, ConsumableModel, 'consumables')
