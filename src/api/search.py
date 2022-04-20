from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.schemas.consumables import Consumable
from src.api.schemas.equipments import Equipment
from src.api.schemas.parts import Part
from src.api.schemas.users import User
from src.database.models import UserModel, EquipmentModel, PartModel, ConsumableModel
from src.database.service import search_by_name
from src.database.sql import get_db

route = APIRouter()


@route.get('/users/{name}',
           response_model=Optional[List[User]],
           response_model_exclude={"password", "is_admin"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=UserModel, name=name)


@route.get('/equipments/{name}',
           response_model=Optional[List[Equipment]],
           response_model_exclude={"contains"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=EquipmentModel, name=name)


@route.get('/parts/{name}',
           response_model=Optional[List[Part]],
           response_model_exclude={"price", "compatibility", "contains"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=PartModel, name=name)


@route.get('/consumables/{name}',
           response_model=Optional[List[Consumable]],
           response_model_exclude={"price", "compatibility", "contains"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=ConsumableModel, name=name)
