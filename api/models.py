from sqlalchemy import Column, Integer, String, Float
from api.database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    lat = Column(Float, index=True)
    long = Column(Float, index=True)


class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    country = Column(String)
    voivodeship = Column(String)
    city = Column(String)
    postal_code = Column(String)
    street = Column(String)
    number = Column(String)