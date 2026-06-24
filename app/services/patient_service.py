from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.patient_schema import Patient, PatientUpdate
from app.db.models import PatientDB


def get_all_patients(db: Session):
    return db.query(PatientDB).all()


def get_patient(patient_id: int, db: Session):
    patient = db.query(PatientDB).filter(
        PatientDB.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


def create_patient(patient: Patient, db: Session):

    new_patient = PatientDB(
        name=patient.name,
        city=patient.city,
        age=patient.age,
        gender=patient.gender,
        height=patient.height,
        weight=patient.weight,
        bmi=patient.bmi,
        weight_category=patient.weight_category
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient Created Successfully",
        "patient_id": new_patient.id
    }


def update_patient(patient_id: int, res: PatientUpdate, db: Session):

    patient = db.query(PatientDB).filter(
        PatientDB.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    updates = res.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(patient, key, value)

    bmi = round(
        patient.weight / (patient.height ** 2),
        2
    )

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    patient.bmi = bmi
    patient.weight_category = category

    db.commit()

    return {"message": "Patient Updated Successfully"}


def delete_patient(patient_id: int, db: Session):

    patient = db.query(PatientDB).filter(
        PatientDB.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return {"message": "Patient Deleted Successfully"}


def sort_patients(sort_by: str, order: str, db: Session):

    valid_sort = ["height", "weight", "bmi"]
    valid_order = ["asc", "desc"]

    if sort_by not in valid_sort:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort field"
        )

    if order not in valid_order:
        raise HTTPException(
            status_code=400,
            detail="Invalid order"
        )

    column = getattr(PatientDB, sort_by)

    if order == "asc":
        return db.query(PatientDB).order_by(column.asc()).all()

    return db.query(PatientDB).order_by(column.desc()).all()