from fastapi import Depends, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session
from api.schemas.parts import PartCreate, Part
from database.models.parts import PartModel
from database.sql import get_db


route = SQLAlchemyCRUDRouter(
    schema=Part,
    create_schema=PartCreate,
    db_model=PartModel,
    db=get_db,
    prefix='parts',
    create_route=False,
    delete_all_route=False
)


@route.post('/')
async def create_part(part: PartCreate, db: Session = Depends(get_db)):
    if db.query(PartModel).filter(PartModel.name == part.name).first():
        raise HTTPException(status_code=400, detail=f'Part {part.name} already exist')
    db.add(PartModel(name=part.name, price=part.price, compatibility=part.compatibility))
    return {'msg': f'Part {part.name} added'}
