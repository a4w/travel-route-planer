import math


class City:
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.flights = list()

    def __str__(self):
        return self.name

    def addFlight(self, trip):
        self.flights.append(trip)

    def __eq__(self, other):
        return self.name == other.name

    def getFlights(self):
        return self.flights

    @staticmethod
    def distance(source, destination) -> float:
        return math.sqrt((source.latitude - destination.latitude)**2 + (source.longitude - destination.longitude)**2)

    def distanceTo(self, city) -> float:
        return City.distance(self, city)

    def __hash__(self):
        return self.name.__hash__()

    def __gt__(self, value):
        return False
