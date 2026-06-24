from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Base(DeclarativeBase):
    pass


class CityDB(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    city_name = Column(String, unique=True, nullable=False)

    patients = relationship(
        "PatientDB",
        back_populates="city"
    )


class PatientDB(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    name = Column(String, nullable=False)

    city_id = Column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False
    )

    age = Column(Integer, nullable=False)

    gender = Column(String, nullable=False)

    # Stored in meters
    height = Column(Float, nullable=False)

    # Stored in kilograms
    weight = Column(Float, nullable=False)

    bmi = Column(Float, nullable=False)

    weight_category = Column(String, nullable=False)

    city = relationship(
        "CityDB",
        back_populates="patients"
    )