from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.authorization import AuthHandler
from src.api.schemas.users import UserCreate, UserLogin
from src.database.models import UserModel
from src.database.sql import get_db

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
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user and auth_handler.verify_password(user.password, db_user.password):
        token = auth_handler.encode_token(user.email)
        return {
            'id': db_user.id,
            'name': db_user.name,
            'email': db_user.email,
            'token': token
        }
    raise HTTPException(status_code=401, detail='Invalid username and/or password')


@route.get('/unprotected')
async def unprotected():
    return {'msg': 'Not authenticated'}


@route.get('/protected')
async def protected(name=Depends(auth_handler.auth_wrapper)):
    return {'msg': f'User {name} is authorized'}
