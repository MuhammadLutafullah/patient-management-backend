from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models import CityDB
from app.schemas.city_schema import City


# -------------------------
# Get All Cities
# -------------------------
def get_all_cities(db: Session):
    return db.query(CityDB).all()


# -------------------------
# Get City by ID
# -------------------------
def get_city_by_id(city_id: int, db: Session):
    city = db.query(CityDB).filter(CityDB.id == city_id).first()
    if not city:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )
    return city


# -------------------------
# Create City
# -------------------------
def create_city(city: City, db: Session):
    # check duplicate city
    existing_city = db.query(CityDB).filter(
        CityDB.city_name.ilike(city.city_name)
    ).first()

    if existing_city:
        raise HTTPException(
            status_code=400,
            detail="City already exists"
        )

    new_city = CityDB(
        city_name=city.city_name.strip().title()
    )

    db.add(new_city)
    db.commit()
    db.refresh(new_city)

    return {
        "message": "City created successfully",
        "city_id": new_city.id,
        "city_name": new_city.city_name
    }


# -------------------------
# Delete City
# -------------------------
def delete_city(city_id: int, db: Session):
    city = db.query(CityDB).filter(CityDB.id == city_id).first()
    if not city:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    db.delete(city)
    db.commit()

    return {
        "message": "City deleted successfully"
    }