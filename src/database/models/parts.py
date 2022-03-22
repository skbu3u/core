from sqlalchemy import Column, String, Integer, JSON
from src.database.sql import Base


class PartModel(Base):
    __tablename__ = 'parts'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    compatibility = Column(JSON, default=[])
    parts = Column(JSON, default=[])

