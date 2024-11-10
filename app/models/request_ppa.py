from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class FlightSearchRequest(BaseModel):
    origin: str = Field(..., min_length=3, max_length=3, pattern="^[A-Z]{3}$", example='BOG')
    destination: str = Field(..., min_length=3, max_length=3, pattern="^[A-Z]{3}$", example='MDE')
    travel_date: str = Field(..., example='2024-11-09')
    max_stops: int = Field(1, ge=0)

    @field_validator("travel_date")
    def validate_travel_date(cls, value):
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")