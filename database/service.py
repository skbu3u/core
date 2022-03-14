from database.sql import engine
from database.models.equipment import db

conn = engine.connect()


def insert_values(name, price):
    conn.execute(db.insert().values(part=name, price=price))


def select_values(part_id):
    part = conn.execute(db.select().where(db.c.id == part_id))
    return part.fetchone()


def delete_values(name):
    conn.execute(db.delete().where(db.c.part == name))


def get_values():
    parts = conn.execute(db.select())
    for part in parts:
        print(part)