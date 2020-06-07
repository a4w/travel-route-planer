import csv
from collections import defaultdict
from City import City
from Flight import Flight
from Timestamp import Timestamp


class FlightKnowledgeExtractor:
    def __init__(self, citiesFile, timetableFile):
        # Read cities and save them in list
        self.cities = dict()
        with open(citiesFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                name = row[0]
                lat = row[1]
                long = row[2]
                self.cities[row[0]] = (
                    City(name, float(lat), float(long)))

        # self.flights = list()
        with open(timetableFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                sourceCity = row[0]
                destinationCity = row[1]
                departureTime = row[2]
                arrivalTime = row[3]
                flightNumber = row[4]
                departureDays = row[5]

                # Unroll days
                departureDays = departureDays.strip("[] ").split(",")
                for day in departureDays:
                    # Check if next day arrival
                    arrival = Timestamp.normalizeDay(day)
                    if(Timestamp.normalizeClock(arrivalTime) < Timestamp.normalizeClock(departureTime)):
                        arrival = Timestamp.nextDay(
                            Timestamp.normalizeDay(day))

                    # Add flight
                    flight = Flight(self.cities[sourceCity], self.cities[destinationCity], Timestamp(
                        day, departureTime), Timestamp(Timestamp.restoreDay(arrival), arrivalTime))
                    # self.flights.append(flight)
                    self.cities[sourceCity].addFlight(flight)

    def getCities(self):
        return self.cities
