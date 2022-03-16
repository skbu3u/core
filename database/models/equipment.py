from sqlalchemy import Column, String, Integer
from database.sql import Base


class Equipment(Base):
    __tablename__ = "Equipment"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    part = Column(String)
    price = Column(Integer)


db = Equipment.__table__
