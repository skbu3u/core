from sqlalchemy import Table, Column, ForeignKey, Boolean, Integer, String, JSON
from sqlalchemy.orm import relationship

from src.database.sql import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)


class EquipmentModel(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)

    # parts = relationship("PartModel", back_populates="equipments")
    parts = relationship("PartModel",
                         secondary="equipment_part",
                         backref="equipments")


equipment_part = Table('equipment_part', Base.metadata,
                       Column('equipments_id', ForeignKey('equipments.id'), primary_key=True),
                       Column('parts_id', ForeignKey('parts.id'), primary_key=True)
                       )


class PartModel(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    price = Column(Integer)

    # compatibility = Column(Integer, ForeignKey("equipments.id"))
    # equipments = relationship("EquipmentModel", back_populates="parts")
    # consumables = relationship("ConsumableModel", back_populates="parts")
    compatibility = Column(String)


class ConsumableModel(Base):
    __tablename__ = "consumables"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    price = Column(Integer)

    # compatibility = Column(Integer, ForeignKey("parts.id"))
    # parts = relationship("PartModel", back_populates="consumables")
    compatibility = Column(String)
