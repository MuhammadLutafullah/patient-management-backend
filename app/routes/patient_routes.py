from fastapi import APIRouter, Query, Path, Depends
from sqlalchemy.orm import Session

from app.schemas.patient_schema import Patient, PatientUpdate
from app.services import patient_service as service
from app.db.database import get_db

router = APIRouter()


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all_patients(db)


@router.get("/patient/{patient_id}")
def get_patient(
    patient_id: str = Path(...),
    db: Session = Depends(get_db)
):
    return service.get_patient(patient_id, db)


@router.get("/sort")
def sort(
    sort_by: str = Query(...),
    order: str = Query("asc"),
    db: Session = Depends(get_db)
):
    return service.sort_patients(sort_by, order, db)


@router.post("/create")
def create_patient(
    res: Patient,
    db: Session = Depends(get_db)
):
    return service.create_patient(res, db)


@router.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    res: PatientUpdate,
    db: Session = Depends(get_db)
):
    return service.update_patient(patient_id, res, db)


@router.delete("/delete/{patient_id}")
def delete_patient(
    patient_id: str,
    db: Session = Depends(get_db)
):
    return service.delete_patient(patient_id, db)