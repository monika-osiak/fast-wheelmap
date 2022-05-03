from typing import Optional

from pydantic import BaseModel


class PointBase(BaseModel):
    name: str
    description: Optional[str] = None
    lat: float
    long: float
    plus_code: Optional[str] = None
    category: Optional[str] = None
    active: bool


class PointCreate(PointBase):
    pass


class Point(PointBase):
    id: int

    class Config:
        orm_mode = True


class PlaceBase(BaseModel):
    name: str
    description: Optional[str] = None
    plus_code: Optional[str] = None
    country: str
    voivodeship: str
    city: str
    postal_code: str
    street: str
    number: str
    accessibility: dict


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True
