from database.sql import engine
from database.models.equipment import db

conn = engine.connect()


def insert_values(name, price):
    conn.execute(db.insert().values(part=name, price=price))


def select_values(name):
    conn.execute(db.select().where(db.c.part == name))
    print(db.c.part == 'Cartridge')


def delete_values(name):
    conn.execute(db.delete().where(db.c.part == name))


def get_values():
    parts = db.select()
    result = conn.execute(parts)

    for row in result:
        return row
