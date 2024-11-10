from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from ..services.flight_search import find_all_routes_dfs
from ..data.initial_data import initialize_airports_and_flights

router = APIRouter()
airports = initialize_airports_and_flights()

@router.get("/flights")
def search_flights(
    origin: str = Query(..., min_length=3, max_length=3, regex="^[A-Z]{3}$", example="BOG"),
    destination: str = Query(..., min_length=3, max_length=3, regex="^[A-Z]{3}$", example="MDE"),
    travel_date: str = Query(..., example="2024-11-09"),
    max_stops: int = Query(1, ge=0, example=1)
):
    try:
        travel_date = datetime.strptime(travel_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    
    if origin not in airports:
        raise HTTPException(status_code=400, detail=f"Invalid origin airport code: {origin}")
    if destination not in airports:
        raise HTTPException(status_code=400, detail=f"Invalid destination airport code: {destination}")

    routes = find_all_routes_dfs(origin, destination, airports, travel_date, max_stops)
    routes_sorted = sorted(routes, key=lambda r: r["total_duration"])
    return {"routes": routes_sorted}