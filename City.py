

class City:
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitue = latitude
        self.longitude = longitude
        self.flights = list()

    def __str__(self):
        return self.name

    def addFlight(self, trip):
        self.flights.append(trip)
