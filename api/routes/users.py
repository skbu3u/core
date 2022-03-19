from fastapi_crudrouter import SQLAlchemyCRUDRouter
from api.schemas.users import User, UserCreate
from database.models.users import UserModel
from database.sql import get_db


route = SQLAlchemyCRUDRouter(
    schema=User,
    create_schema=UserCreate,
    db_model=UserModel,
    db=get_db,
    prefix='users',
    create_route=False,
    delete_all_route=False
)
