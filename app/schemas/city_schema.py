from pydantic import BaseModel, Field


class City(BaseModel):
    city_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )


class CityResponse(BaseModel):
    id: int
    city_name: str

    model_config = {
        "from_attributes": True
    }