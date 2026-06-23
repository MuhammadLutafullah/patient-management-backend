import json
from fastapi import HTTPException
from app.schemas.patient_schema import Patient, PatientUpdate
from app.core.config import DB_PATH


# -------------------------
# DB Helpers
# -------------------------
def load_data():
    with open(DB_PATH, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------
# Service Functions
# -------------------------
def get_all_patients():
    return load_data()


def get_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    return data[patient_id]


def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    data[patient.id] = patient.model_dump(exclude=["id"])
    save_data(data)

    return {"message": "Patient Created Successfully"}


def update_patient(patient_id: str, res: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing = data[patient_id]
    updates = res.model_dump(exclude_unset=True)

    for k, v in updates.items():
        existing[k] = v

    # rebuild object to recalculate computed fields
    patient_obj = Patient(id=patient_id, **existing)
    data[patient_id] = patient_obj.model_dump(exclude=["id"])

    save_data(data)

    return {"message": "Patient Updated Successfully"}


def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return {"message": "Patient Deleted Successfully"}


def sort_patients(sort_by: str, order: str):
    valid_sort = ["height", "weight", "bmi"]
    valid_order = ["asc", "desc"]

    if sort_by not in valid_sort:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    if order not in valid_order:
        raise HTTPException(status_code=400, detail="Invalid order")

    data = load_data()
    reverse = order == "desc"

    return sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse
    )