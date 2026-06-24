from pydantic import BaseModel, Field, computed_field
from typing import Literal, Optional


class Patient(BaseModel):
    name: str = Field(..., max_length=21)
    city: str
    age: int
    gender: Literal["male", "female", "other"]
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def weight_category(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[Literal["male", "female", "other"]] = None
    height: Optional[float] = Field(default=None, gt=0)
    weight: Optional[float] = Field(default=None, gt=0)