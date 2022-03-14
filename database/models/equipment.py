from sqlalchemy import Column, String, Integer, DateTime
from database.sql import Base


class Equipment(Base):
    __tablename__ = "Equipment"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    part = Column(String)
    price = Column(Integer)
    date = Column(DateTime)


db = Equipment.__table__
