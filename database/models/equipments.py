from sqlalchemy import Column, String, Integer, JSON
from database.sql import Base


class EquipmentModel(Base):
    __tablename__ = 'equipments'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    parts = Column(JSON)
