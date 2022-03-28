from fastapi import Depends, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session

from src.api.schemas.consumables import Consumable, ConsumableCreate
from src.api.schemas.equipments import Equipment, EquipmentCreate
from src.api.schemas.parts import Part, PartCreate
from src.api.schemas.users import User, UserCreate
from src.database.models import ConsumableModel
from src.database.models import EquipmentModel
from src.database.models import PartModel
from src.database.models import UserModel
from src.database.sql import get_db


def add_route(schema, create_schema, db_model, prefix, create_route=False):
    route = SQLAlchemyCRUDRouter(
        schema=schema,
        create_schema=create_schema,
        db_model=db_model,
        db=get_db,
        prefix=prefix,
        create_route=create_route
    )
    return route


users = add_route(User, UserCreate, UserModel, 'users')
equipments = add_route(Equipment, EquipmentCreate, EquipmentModel, 'equipments')
parts = add_route(Part, PartCreate, PartModel, 'parts')
consumables = add_route(Consumable, ConsumableCreate, ConsumableModel, 'consumables')


@equipments.post("/", response_model=Equipment)
def create_one(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = db.query(EquipmentModel).filter(EquipmentModel.name == equipment.name).first()
    if db_equipment:
        raise HTTPException(status_code=400, detail=f"{equipment.name} already exist")
    db_equipment = EquipmentModel(name=equipment.name)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


@parts.post("/{compatibility}", response_model=Equipment)
def create_one(compatibility: str, part: PartCreate, db: Session = Depends(get_db)):
    db_equipment = db.query(EquipmentModel).filter(EquipmentModel.name == compatibility).first()
    db_part = PartModel(**part.dict(), compatibility=compatibility)
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    if db_equipment:
        db_equipment.parts.append(db_part)
    return db_part


@consumables.post("/{compatibility}", response_model=Part)
def create_one(compatibility: str, consumable: ConsumableCreate, db: Session = Depends(get_db)):
    db_part = db.query(PartModel).filter(PartModel.name == compatibility).first()
    db_consumable = ConsumableModel(**consumable.dict(), compatibility=compatibility)
    db.add(db_consumable)
    db.commit()
    db.refresh(db_consumable)
    if db_part:
        db_part.consumables.append(db_consumable)
    return db_consumable
