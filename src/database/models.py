from sqlalchemy import Table, Column, ForeignKey, Boolean, Integer, String
from sqlalchemy.orm import relationship

from src.database.sql import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)


class EquipmentModel(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    contains = relationship("PartModel",
                            secondary="equipment_part",
                            backref="equipments")

    def __repr__(self):
        return "{'name': '%s', 'contains': %s}" % (self.name, self.contains)


equipment_part = Table('equipment_part', Base.metadata,
                       Column('equipments_id', ForeignKey('equipments.id'), primary_key=True),
                       Column('parts_id', ForeignKey('parts.id'), primary_key=True)
                       )


class PartModel(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    compatibility = Column(String)
    contains = relationship("ConsumableModel",
                            secondary="part_consumable",
                            backref="parts")

    def __repr__(self):
        return "{'name': '%s', 'Price': %s, 'contains': %s}" % (self.name, self.price, self.contains)


part_consumable = Table('part_consumable', Base.metadata,
                        Column('parts_id', ForeignKey('parts.id'), primary_key=True),
                        Column('consumables_id', ForeignKey('consumables.id'), primary_key=True)
                        )


class ConsumableModel(Base):
    __tablename__ = "consumables"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    compatibility = Column(String)

    def __repr__(self):
        return "{'name': '%s', 'Price': %s}" % (self.name, self.price)
