from pydantic import BaseModel

class FareRequest(BaseModel):
    origin: str | None = None  # Optional if distance is provided
    destination: str | None = None  # Optional if distance is provided
    distance: float | None = None  # Required if no origin/destination
    unit: str  # "km" or "miles"

class FareResponse(BaseModel):
    estimated_fare: float
    currency: str
