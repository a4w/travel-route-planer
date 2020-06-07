from City import City
from Timestamp import Timestamp


class Flight:
    def __init__(self, sourceCity: City, destinationCity: City, departure: Timestamp, arrival: Timestamp):
        self.sourceCity = sourceCity
        self.destinationCity = destinationCity
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return "From " + str(self.sourceCity) + " to " + str(self.destinationCity) + ", departure: " + str(self.departure) + ", arrival: " + str(self.arrival)

