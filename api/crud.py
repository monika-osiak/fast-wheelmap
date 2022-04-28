from sqlalchemy.orm import Session

from . import models, schemas


def create_point(db: Session, point: schemas.PointCreate):
    db_point = models.Point(
        name=point.name,
        description=point.description,
        lat=point.lat,
        long=point.long
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


def get_point(db: Session, point_id: int):
    return db.query(models.Point).filter(models.Point.id == point_id).first()


def get_point_by_lat_long(db: Session, lat: float, long: float):
    return db.query(models.Point)\
        .filter(models.Point.lat == lat)\
        .filter(models.Point.long == long)\
        .first()


def get_points(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Point).offset(skip).limit(limit).all()


def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(
        name=place.name,
        description=place.description,
        country=place.country,
        voivodeship=place.voivodeship,
        city=place.city,
        postal_code=place.postal_code,
        street=place.street,
        number=place.number
    )
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()


def get_place_by_address(
        db: Session,
        country: str,
        voivodeship: str,
        city: str,
        postal_code: str,
        street: str,
        number: str
    ):
    return db.query(models.Place)\
        .filter(models.Place.country == country)\
        .filter(models.Place.voivodeship == voivodeship) \
        .filter(models.Place.city == city) \
        .filter(models.Place.postal_code == postal_code) \
        .filter(models.Place.street == street) \
        .filter(models.Place.number == number) \
        .first()


def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()
