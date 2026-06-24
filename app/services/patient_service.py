from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.patient_schema import Patient, PatientUpdate
from app.db.models import PatientDB, CityDB


def convert_height_to_meters(height: float, unit: str):
    if unit == "cm":
        return height / 100
    if unit == "inch":
        return height * 0.0254
    if unit == "feet":
        return height * 0.3048
    raise HTTPException(
        status_code=400,
        detail="Invalid height unit"
    )


def convert_weight_to_kg(weight: float, unit: str):
    if unit == "kg":
        return weight
    if unit == "lbs":
        return weight * 0.453592
    raise HTTPException(
        status_code=400,
        detail="Invalid weight unit"
    )


def calculate_bmi(height: float, weight: float):
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


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
    city = db.query(CityDB).filter(
        CityDB.id == patient.city_id
    ).first()
    if not city:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    height_in_meters = convert_height_to_meters(
        patient.height,
        patient.height_unit
    )
    weight_in_kg = convert_weight_to_kg(
        patient.weight,
        patient.weight_unit
    )
    bmi, category = calculate_bmi(
        height_in_meters,
        weight_in_kg
    )

    new_patient = PatientDB(
        name=patient.name,
        city_id=patient.city_id,
        age=patient.age,
        gender=patient.gender,
        height=height_in_meters,
        weight=weight_in_kg,
        bmi=bmi,
        weight_category=category
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

    if "city_id" in updates:
        city = db.query(CityDB).filter(
            CityDB.id == updates["city_id"]
        ).first()
        if not city:
            raise HTTPException(
                status_code=404,
                detail="City not found"
            )

    if "height" in updates and "height_unit" in updates:
        updates["height"] = convert_height_to_meters(
            updates["height"],
            updates["height_unit"]
        )

    if "weight" in updates and "weight_unit" in updates:
        updates["weight"] = convert_weight_to_kg(
            updates["weight"],
            updates["weight_unit"]
        )

    updates.pop("height_unit", None)
    updates.pop("weight_unit", None)

    for key, value in updates.items():
        setattr(patient, key, value)

    bmi, category = calculate_bmi(
        patient.height,
        patient.weight
    )
    patient.bmi = bmi
    patient.weight_category = category

    db.commit()

    return {
        "message": "Patient Updated Successfully"
    }


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

    return {
        "message": "Patient Deleted Successfully"
    }


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
        return db.query(PatientDB).order_by(
            column.asc()
        ).all()
    return db.query(PatientDB).order_by(
        column.desc()
    ).all()