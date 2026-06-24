from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.city_schema import City, CityResponse
from app.services import city_service as service

router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)


# -------------------------
# Get all cities
# -------------------------
@router.get("/", response_model=list[CityResponse])
def get_all_cities(db: Session = Depends(get_db)):
    return service.get_all_cities(db)


# -------------------------
# Get city by ID
# -------------------------
@router.get("/{city_id}", response_model=CityResponse)
def get_city(
    city_id: int = Path(...),
    db: Session = Depends(get_db)
):
    return service.get_city_by_id(city_id, db)


# -------------------------
# Create city
# -------------------------
@router.post("/", response_model=dict)
def create_city(
    city: City,
    db: Session = Depends(get_db)
):
    return service.create_city(city, db)


# -------------------------
# Delete city
# -------------------------
@router.delete("/{city_id}", response_model=dict)
def delete_city(
    city_id: int,
    db: Session = Depends(get_db)
):
    return service.delete_city(city_id, db)