from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import FareRequest, FareResponse
from services import calculate_fare, get_distance
from models import FareHistory

# Initialize FastAPI App
app = FastAPI()

# # Create database tables
# Base.metadata.create_all(bind=engine)

# @app.post("/calculate_fare/", response_model=FareResponse)
# def calculate_fare_api(request: FareRequest, db: Session = Depends(get_db)):
#     if request.origin and request.destination:
#         request.distance = get_distance(request.origin, request.destination)

#     if not request.distance:
#         raise HTTPException(status_code=400, detail="Distance is required")

#     estimated_fare = calculate_fare(request.distance, request.unit, db)
    
#     # Save to database
#     fare_entry = FareHistory(
#         origin=request.origin,
#         destination=request.destination,
#         distance=request.distance,
#         unit=request.unit,
#         fare=estimated_fare
#     )
#     db.add(fare_entry)
#     db.commit()

#     return {"estimated_fare": estimated_fare, "currency": "NGN"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Nigerian Fare Calculator API"}
