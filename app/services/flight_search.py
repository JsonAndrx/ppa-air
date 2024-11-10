from typing import List, Dict
from datetime import timedelta, datetime
from ..models.flight import Flight

def find_all_routes_dfs(origin: str, destination: str, airports: dict, travel_date: datetime, max_stops: int = 2):
    routes = []
    dfs_find_routes(origin, destination, airports, [], routes, max_stops, timedelta(), travel_date)
    return routes

def dfs_find_routes(current: str, destination: str, airports: dict, path: List[Flight], routes: List[Dict], max_stops: int, total_duration: timedelta, travel_date: datetime):
    if current == destination:
        route_info = {
            "segments": [
                {
                    "origin": flight.origin,
                    "destination": flight.destination,
                    "departure_time": flight.departure_time.strftime("%Y-%m-%d %H:%M"),
                    "arrival_time": (flight.departure_time + timedelta(minutes=flight.duration)).strftime("%Y-%m-%d %H:%M"),
                    "duration": flight.duration
                } for flight in path
            ],
            "total_duration": total_duration.total_seconds() // 60
        }
        routes.append(route_info)
        return

    if len(path) > max_stops:
        return

    for flight in airports[current].connections:
        if flight.departure_time.date() == travel_date.date() and not any(f.destination == flight.destination for f in path):
            path.append(flight)
            dfs_find_routes(
                flight.destination,
                destination,
                airports,
                path,
                routes,
                max_stops,
                total_duration + timedelta(minutes=flight.duration),
                travel_date
            )
            path.pop()