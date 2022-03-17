from database.sql import connection
from database.models.equipment import db


def insert_values(name, price):
    connection.execute(db.insert().values(part=name, price=price))


def select_values(part_id):
    part = connection.execute(db.select().where(db.c.id == part_id))
    return part.fetchone()


def delete_values(name):
    connection.execute(db.delete().where(db.c.part == name))


def get_values():
    parts = connection.execute(db.select())
    for part in parts:
        print(part)
