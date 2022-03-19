from fastapi import APIRouter, Depends, HTTPException
from api.authorization import AuthHandler
from api.schemas.users import UserCreate
from database.sql import connection
from database.models.users import users

security_route = APIRouter()
auth_handler = AuthHandler()


@security_route.post('/register', status_code=201)
async def register_new_user(user: UserCreate):
    if connection.execute(users.select().where(users.c.name == user.name)).fetchall():
        raise HTTPException(status_code=400, detail=f'Username {user.name} is taken')
    hashed_password = auth_handler.get_password_hash(user.password)
    connection.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=hashed_password
    ))
    return {'msg': f'User {user.name} created'}


@security_route.post('/login')
async def login(user: UserCreate):
    auth = connection.execute(users.select().where(users.c.name == user.name)).fetchall()
    if auth and auth_handler.verify_password(user.password, auth[0][3]):
        token = auth_handler.encode_token(user.name)
        return {'token': token}
    raise HTTPException(status_code=401, detail='Invalid username and/or password')


@security_route.get('/unprotected')
async def unprotected():
    return {'msg': 'Not authenticated'}


@security_route.get('/protected')
async def protected(name=Depends(auth_handler.auth_wrapper)):
    return {'msg': f'User {name} is authorized'}
