from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.schemas.equipments import Equipment
from src.api.schemas.parts import PartCreate
from src.database.crud.parts import get_parts, create_equipment_part
from src.database.sql import get_db

# route = SQLAlchemyCRUDRouter(
#     schema=Part,
#     create_schema=PartCreate,
#     db_model=PartModel,
#     db=get_db,
#     prefix='parts',
#     create_route=False,
#     delete_all_route=False
# )

route = APIRouter()


@route.get("/parts/", response_model=List[Equipment])
def get_all_parts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    parts = get_parts(db, skip=skip, limit=limit)
    return parts


@route.post("/equipments/{compatibility}/parts/", response_model=Equipment)
def create_part_for_equipment(
    compatibility: str, part: PartCreate, db: Session = Depends(get_db)
):
    compatibility = ", ".join(compatibility.replace(',', ' ').strip().lower().title().split())
    return create_equipment_part(db=db, part=part, compatibility=compatibility)
