from fastapi import APIRouter, Depends, HTTPException
from api.auth import AuthHandler
from api.schemas.users import AuthDetails
from database.sql import connection
from database.models.users import users

security_route = APIRouter()
auth_handler = AuthHandler()
users_base = []


@security_route.post('/register', status_code=201)
async def register(auth_details: AuthDetails):
    if connection.execute(users.select().where(users.c.name == auth_details.username)).fetchall():
        raise HTTPException(status_code=400, detail=f'Username {auth_details.username} is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    connection.execute(users.insert().values(
        name=auth_details.username,
        email=auth_details.email,
        password=hashed_password
    ))
    return {'msg': f'User {auth_details.username} created'}


@security_route.post('/login')
async def login(auth_details: AuthDetails):
    auth = connection.execute(users.select().where(users.c.name == auth_details.username)).fetchall()
    if auth and auth_handler.verify_password(auth_details.password, auth[0][3]):
        token = auth_handler.encode_token(auth_details.username)
        return {'token': token}
    raise HTTPException(status_code=401, detail='Invalid username and/or password')


@security_route.get('/unprotected')
async def unprotected():
    return {'msg': 'Not authenticated'}


@security_route.get('/protected')
async def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}
