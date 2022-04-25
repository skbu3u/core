from typing import Optional, List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.api.schemas.consumables import Consumable
from src.api.schemas.equipments import Equipment
from src.api.schemas.parts import Part
from src.api.schemas.users import User
from src.database.models import UserModel, EquipmentModel, PartModel, ConsumableModel
from src.database.service import search_by_name
from src.database.sql import get_db

search = APIRouter()


@search.get('/users/{name}',
            response_model=Optional[List[User]],
            response_model_exclude={"password", "is_admin"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=UserModel, name=name)


@search.get('/equipments/{name}',
            response_model=Optional[List[Equipment]],
            response_model_exclude={"contains"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=EquipmentModel, name=name)


@search.get('/parts/{name}',
            response_model=Optional[List[Part]],
            response_model_exclude={"price", "compatibility", "contains"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=PartModel, name=name)


@search.get('/consumables/{name}',
            response_model=Optional[List[Consumable]],
            response_model_exclude={"price", "compatibility", "contains"})
def get_all_matches(name: str, db: Session = Depends(get_db)):
    return search_by_name(db=db, model=ConsumableModel, name=name)
