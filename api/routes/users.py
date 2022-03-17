from fastapi import APIRouter
from database.sql import connection
from database.models.users import users
from api.schemas.users import User

users_route = APIRouter()


@users_route.get('/')  # response_model=User
async def read_all():
    response = connection.execute(users.select()).fetchall()
    if response:
        return response
    else:
        return {'msg': 'There are no users in the database'}


@users_route.post('/')
async def write(user: User):
    connection.execute(users.insert().values(
        about=user.about
    ))
    return connection.execute(users.select()).fetchall()


@users_route.get('/{user_id}')
async def read(user_id: int):
    response = connection.execute(users.select().where(users.c.id == user_id)).fetchall()
    if response:
        return response
    else:
        return {'msg': 'There is no user with this ID in the database'}


@users_route.put('/{user_id}')
async def update(user_id: int, user: User):
    connection.execute(users.update().values(
        about=user.about
    ).where(users.c.id == user_id))
    return connection.execute(users.select()).fetchall()


@users_route.delete('/{user_id}')
async def delete(user_id: int):
    connection.execute(users.delete().where(users.c.id == user_id))
    return connection.execute(users.select()).fetchall()
