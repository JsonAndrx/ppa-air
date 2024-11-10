from datetime import datetime
from ..models.flight import Airport, Flight

def initialize_airports_and_flights():
    airports = {
        "BOG": Airport("BOG"),
        "MDE": Airport("MDE"),
        "BAQ": Airport("BAQ"),
        "BGA": Airport("BGA"),
        "SMR": Airport("SMR"),
        "CTG": Airport("CTG"),
        "CLO": Airport("CLO"),
        "EOH": Airport("EOH"),
    }

    flights = [
        Flight("BOG", "MDE", 60, datetime(2024, 11, 9, 6, 0)),
        Flight("MDE", "BOG", 60, datetime(2024, 11, 9, 8, 0)),
        Flight("BOG", "BAQ", 90, datetime(2024, 11, 9, 9, 0)),
        Flight("BAQ", "BOG", 90, datetime(2024, 11, 9, 11, 0)),
        Flight("BOG", "CTG", 75, datetime(2024, 11, 9, 12, 0)),
        Flight("CTG", "BOG", 75, datetime(2024, 11, 9, 14, 0)),
        Flight("MDE", "BAQ", 120, datetime(2024, 11, 9, 10, 0)),
        Flight("BAQ", "MDE", 120, datetime(2024, 11, 9, 13, 0)),
        Flight("MDE", "CLO", 45, datetime(2024, 11, 9, 7, 30)),
        Flight("CLO", "MDE", 45, datetime(2024, 11, 9, 9, 0)),
        Flight("CTG", "SMR", 30, datetime(2024, 11, 9, 15, 0)),
        Flight("SMR", "CTG", 30, datetime(2024, 11, 9, 16, 0)),
        Flight("CLO", "BGA", 60, datetime(2024, 11, 9, 17, 0)),
        Flight("BGA", "CLO", 60, datetime(2024, 11, 9, 18, 0)),
        Flight("BOG", "EOH", 45, datetime(2024, 11, 9, 8, 30)),
        Flight("EOH", "BOG", 45, datetime(2024, 11, 9, 10, 0)),
    ]

    for flight in flights:
        airports[flight.origin].connections.append(flight)

    return airports
