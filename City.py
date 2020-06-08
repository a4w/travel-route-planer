from math import sin, cos, sqrt, atan2, radians


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
        # approximate radius of earth in km
        R = 6373.0
        lat1 = radians(source.latitude)
        lon1 = radians(source.longitude)
        lat2 = radians(destination.latitude)
        lon2 = radians(destination.longitude)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    def distanceTo(self, city) -> float:
        return City.distance(self, city)

    def __hash__(self):
        return self.name.__hash__()

    def __gt__(self, value):
        return False
