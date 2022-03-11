from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///test.db', echo=True)
conn = engine.connect()
meta = MetaData()

part = Table(
    'part', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Integer),
)


def create_table():
    meta.create_all(engine)


def insert_values(name, price):
    conn.execute(part.insert().values(name=name, price=price))


def print_values():
    parts = part.select()
    result = conn.execute(parts)

    for row in result:
        print(row)


def delete_values():
    conn.execute(part.delete().where(part.c.name == 'Toner'))


# insert_values('Cartridge', 50)
# insert_values('Toner', 10)
delete_values()
print_values()
