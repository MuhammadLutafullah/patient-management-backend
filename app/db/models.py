from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, Float


class Base(DeclarativeBase):
    pass


class PatientDB(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    bmi = Column(Float, nullable=False)
    weight_category = Column(String, nullable=False)