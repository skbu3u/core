from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.schemas.consumables import ConsumableCreate
from src.api.schemas.parts import Part
from src.database.crud.consumables import get_consumables, create_part_consumable
from src.database.sql import get_db

route = APIRouter()


@route.get("/consumables/", response_model=list[Part])
def get_all_consumables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_consumables(db, skip=skip, limit=limit)


@route.post("/parts/{compatibility}/consumables/", response_model=Part)
def create_consumable_for_part(
    compatibility: str, consumable: ConsumableCreate, db: Session = Depends(get_db)
):
    compatibility = ", ".join(compatibility.replace(',', ' ').strip().lower().title().split())
    return create_part_consumable(db=db, consumable=consumable, compatibility=compatibility)
