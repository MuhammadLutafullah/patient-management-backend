from fastapi import APIRouter, Query, Path
from app.schemas.patient_schema import Patient, PatientUpdate
from app.services import patient_service as service

router = APIRouter()


@router.get("/")
def get_all():
    return service.get_all_patients()


@router.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(...)):
    return service.get_patient(patient_id)


@router.get("/sort")
def sort(
    sort_by: str = Query(...),
    order: str = Query("asc")
):
    return service.sort_patients(sort_by, order)


@router.post("/create")
def create_patient(res: Patient):
    return service.create_patient(res)


@router.put("/edit/{patient_id}")
def update_patient(patient_id: str, res: PatientUpdate):
    return service.update_patient(patient_id, res)


@router.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    return service.delete_patient(patient_id)