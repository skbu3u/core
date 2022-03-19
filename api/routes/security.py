from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.authorization import AuthHandler
from api.schemas.users import UserCreate
from database.models.users import UserModel
from database.sql import get_db

route = APIRouter()
auth_handler = AuthHandler()


@route.post('/register', status_code=201)
async def register_new_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(UserModel).filter(UserModel.name == user.name).first():
        raise HTTPException(status_code=400, detail=f'Username {user.name} is taken')
    hashed_password = auth_handler.get_password_hash(user.password)
    db.add(UserModel(name=user.name, email=user.email, password=hashed_password))
    return {'msg': f'User {user.name} created'}


@route.post('/login')
async def login(user: UserCreate, db: Session = Depends(get_db)):
    auth = db.query(UserModel).filter(UserModel.name == user.name).first()
    if auth and auth_handler.verify_password(user.password, auth.password):
        token = auth_handler.encode_token(user.name)
        return {'token': token}
    raise HTTPException(status_code=401, detail='Invalid username and/or password')


@route.get('/unprotected')
async def unprotected():
    return {'msg': 'Not authenticated'}


@route.get('/protected')
async def protected(name=Depends(auth_handler.auth_wrapper)):
    return {'msg': f'User {name} is authorized'}
