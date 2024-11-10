from datetime import datetime

class Airport:
    def __init__(self, code: str):
        self.code = code
        self.connections = []

class Flight:
    def __init__(self, origin: str, destination: str, duration: int, departure_time: datetime):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.departure_time = departure_time
