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


@equipments.post("", response_model=Equipment)
def create_one(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = db.query(EquipmentModel).filter(EquipmentModel.name == equipment.name).first()
    if db_equipment:
        raise HTTPException(status_code=400, detail=f"{equipment.name} already exist")
    db_equipment = EquipmentModel(name=equipment.name)
    if isinstance(db_equipment, EquipmentModel):
        db.add(db_equipment)
        db.commit()
        db.refresh(db_equipment)
    return db_equipment


@parts.post("", response_model=Equipment)
def create_one(part: PartCreate, db: Session = Depends(get_db)):
    db_part = db.query(PartModel).filter(PartModel.name == part.name).first()
    if db_part:
        raise HTTPException(status_code=400, detail=f"{part.name} already exist")
    db_part = PartModel(**part.dict())
    if isinstance(db_part, PartModel):
        db.add(db_part)
        db.commit()
        db.refresh(db_part)
    compatibility_list = [i.strip().lower() for i in part.compatibility.split(",")]
    for compatibility in compatibility_list:
        db_equipment = db.query(EquipmentModel).filter(EquipmentModel.name == compatibility).first()
        if db_equipment:
            db_equipment.parts.append(db_part)
    return db_part


@consumables.post("", response_model=Part)
def create_one(consumable: ConsumableCreate, db: Session = Depends(get_db)):
    db_consumable = db.query(ConsumableModel).filter(ConsumableModel.name == consumable.name).first()
    if db_consumable:
        raise HTTPException(status_code=400, detail=f"{consumable.name} already exist")
    db_consumable = ConsumableModel(**consumable.dict())
    if isinstance(db_consumable, ConsumableModel):
        db.add(db_consumable)
        db.commit()
        db.refresh(db_consumable)
    compatibility_list = [i.strip().lower() for i in consumable.compatibility.split(",")]
    for compatibility in compatibility_list:
        db_part = db.query(PartModel).filter(PartModel.name == compatibility).first()
        if db_part:
            db_part.consumables.append(db_consumable)
    return db_consumable
