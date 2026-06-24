from pydantic import BaseModel, Field
from typing import Literal, Optional


class Patient(BaseModel):
    name: str = Field(..., max_length=21)

    # Foreign key from cities table
    city_id: int

    age: int

    gender: Literal["male", "female", "other"]

    height: float = Field(..., gt=0)

    height_unit: Literal["cm", "inch", "feet"]

    weight: float = Field(..., gt=0)

    weight_unit: Literal["kg", "lbs"]


class PatientUpdate(BaseModel):
    name: Optional[str] = None

    city_id: Optional[int] = None

    age: Optional[int] = None

    gender: Optional[Literal["male", "female", "other"]] = None

    height: Optional[float] = Field(default=None, gt=0)

    height_unit: Optional[Literal["cm", "inch", "feet"]] = None

    weight: Optional[float] = Field(default=None, gt=0)

    weight_unit: Optional[Literal["kg", "lbs"]] = None