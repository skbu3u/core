from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.authorization import AuthHandler
from src.api.schemas.users import UserCreate
from src.database.models import UserModel
from src.database.service import add_to_db, check_exist_in_db
from src.database.sql import get_db

route = APIRouter()


@route.post('/register', status_code=201)
def register_new_user(user: UserCreate, db: Session = Depends(get_db)):
    check_exist_in_db(db=db, schema=user, model=UserModel)
    new_user = UserModel(name=user.name, password=AuthHandler().get_password_hash(user.password))
    add_to_db(db=db, model=UserModel, new_model=new_user)
    return new_user, {'msg': f'User {new_user.name} created'}


@route.post('/login')
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.name == user.name).first()
    if db_user and AuthHandler().verify_password(user.password, db_user.password):
        token = AuthHandler().encode_token(user.name)
        return db_user, {'token': token}
    raise HTTPException(status_code=401, detail='Invalid username and/or password')


@route.get('/unprotected')
def unprotected():
    return {'msg': 'Not authenticated'}


@route.get('/protected')
def protected(name=Depends(AuthHandler().auth_wrapper)):
    return {'msg': f'User {name} is authorized'}
