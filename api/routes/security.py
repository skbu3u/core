from fastapi import APIRouter, Depends, HTTPException
from api.authorization import AuthHandler
from api.schemas.users import User
from database.sql import connection
from database.models.users import users

security_route = APIRouter()
auth_handler = AuthHandler()
users_base = []


@security_route.post('/register', status_code=201)
async def register(user: User):
    if connection.execute(users.select().where(users.c.name == user.username)).fetchall():
        raise HTTPException(status_code=400, detail=f'Username {user.username} is taken')
    hashed_password = auth_handler.get_password_hash(user.password)
    connection.execute(users.insert().values(
        name=user.username,
        email=user.email,
        password=hashed_password
    ))
    return {'msg': f'User {user.username} created'}


@security_route.post('/login')
async def login(user: User):
    auth = connection.execute(users.select().where(users.c.name == user.username)).fetchall()
    if auth and auth_handler.verify_password(user.password, auth[0][3]):
        token = auth_handler.encode_token(user.username)
        return {'token': token}
    raise HTTPException(status_code=401, detail='Invalid username and/or password')


@security_route.get('/unprotected')
async def unprotected():
    return {'msg': 'Not authenticated'}


@security_route.get('/protected')
async def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'msg': f'User {username} is authorized'}
