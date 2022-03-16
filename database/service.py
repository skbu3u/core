from database.sql import connect
from database.models.equipment import db


def insert_values(name, price):
    connect.execute(db.insert().values(part=name, price=price))


def select_values(part_id):
    part = connect.execute(db.select().where(db.c.id == part_id))
    return part.fetchone()


def delete_values(name):
    connect.execute(db.delete().where(db.c.part == name))


def get_values():
    parts = connect.execute(db.select())
    for part in parts:
        print(part)
