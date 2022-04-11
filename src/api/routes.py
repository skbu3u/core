from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session

from src.api.authorization import AuthHandler
from src.api.schemas.consumables import Consumable, ConsumableCreate
from src.api.schemas.equipments import Equipment, EquipmentCreate
from src.api.schemas.parts import Part, PartCreate
from src.api.schemas.users import User, UserCreate
from src.database.models import ConsumableModel
from src.database.models import EquipmentModel
from src.database.models import PartModel
from src.database.models import UserModel
from src.database.service import check_exist_in_db, add_to_db, check_compatibility
from src.database.sql import get_db


def add_route(schema, create_schema, db_model, prefix, create_route=False):
    route = SQLAlchemyCRUDRouter(
        schema=schema,
        create_schema=create_schema,
        db_model=db_model,
        db=get_db,
        prefix=prefix,
        create_route=create_route,
        dependencies=[Depends(AuthHandler().auth_wrapper)]
    )
    return route


users = add_route(User, UserCreate, UserModel, 'users')
equipments = add_route(Equipment, EquipmentCreate, EquipmentModel, 'equipments')
parts = add_route(Part, PartCreate, PartModel, 'parts')
consumables = add_route(Consumable, ConsumableCreate, ConsumableModel, 'consumables')


@equipments.post("", response_model=Equipment)
def create_one(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=equipment, model=EquipmentModel)
    new_equipment = EquipmentModel(name=equipment.name)
    add_to_db(db=db, model=EquipmentModel, new_model=new_equipment)
    return new_equipment


@parts.post("", response_model=Equipment)
def create_one(part: PartCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=part, model=PartModel)
    new_part = PartModel(**part.dict())
    add_to_db(db=db, model=PartModel, new_model=new_part)
    check_compatibility(db=db, schema=part, model=EquipmentModel, new_model=new_part)
    return new_part


@consumables.post("", response_model=Part)
def create_one(consumable: ConsumableCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=consumable, model=ConsumableModel)
    new_consumable = ConsumableModel(**consumable.dict())
    add_to_db(db=db, model=ConsumableModel, new_model=new_consumable)
    check_compatibility(db=db, schema=consumable, model=PartModel, new_model=new_consumable)
    return new_consumable
