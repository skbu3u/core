from fastapi_crudrouter import SQLAlchemyCRUDRouter
from api.schemas.parts import PartCreate, Part
from database.models.parts import PartModel
from database.sql import get_db


route = SQLAlchemyCRUDRouter(
    schema=Part,
    create_schema=PartCreate,
    db_model=PartModel,
    db=get_db,
    prefix='parts'
)
