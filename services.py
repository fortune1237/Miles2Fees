import googlemaps
import requests
from config import GOOGLE_MAPS_API_KEY, USD_TO_NGN
from sqlalchemy.orm import Session
from models import FareHistory

gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def get_distance(origin: str, destination: str) -> float:
    """Get distance between two locations using Google Maps API"""
    directions = gmaps.directions(origin, destination)
    distance_km = directions[0]["legs"][0]["distance"]["value"] / 1000
    return distance_km

def get_exchange_rate() -> float:
    """Get real-time exchange rate from USD to NGN"""
    url = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"
    response = requests.get(url).json()
    return response["conversion_rates"].get("NGN", USD_TO_NGN)

def calculate_fare(distance: float, unit: str, db: Session):
    """Calculate fare based on distance and save to database"""
    base_fare = 5  # Base charge
    rate_per_km = 2
    rate_per_mile = 3.22

    fare = base_fare + (distance * rate_per_km if unit == "km" else distance * rate_per_mile)
    
    # Convert to NGN
    exchange_rate = get_exchange_rate()
    fare_ngn = round(fare * exchange_rate, 2)

    return fare_ngn
