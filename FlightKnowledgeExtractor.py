import csv
import networkx as nx
import matplotlib.pyplot as plt
import time
from collections import defaultdict
from City import City
from Flight import Flight
from Timestamp import Timestamp


class FlightKnowledgeExtractor:

    def updateGraph(self, wait=0.5):
        time.sleep(wait)
        plt.clf()
        colors = [self.graph.nodes[name]["node_color"]
                  for name in self.graph.nodes()]
        pos = nx.get_node_attributes(self.graph, 'pos')
        nx.draw_networkx(self.graph, with_labels=True,
                         node_color=colors, pos=pos)
        plt.draw()
        plt.pause(0.01)

    def resetGraph(self):
        for n in self.graph.nodes():
            self.graph.nodes[n]["node_color"] = '#CCCCCC'

    def visitGraphNode(self, city, end=False):
        if(end):
            self.graph.nodes[city]["node_color"] = "#000000"
        else:
            self.graph.nodes[city]["node_color"] = "#0095ff"

        self.updateGraph()

    def markAvailableGraphNode(self, city):
        self.graph.nodes[city]["node_color"] = "#00FF00"
        self.updateGraph()

    def closeVisualizer(self):
        plt.close()

    def __init__(self, citiesFile, timetableFile):
        # Read cities and save them in list
        self.cities = dict()
        self.graph = nx.Graph()
        with open(citiesFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                name = row[0]
                lat = row[1]
                long = row[2]
                self.cities[name] = (
                    City(name, float(lat), float(long)))
                self.graph.add_node(name, pos=(float(lat), float(long)))
                self.graph.nodes[name]["node_color"] = '#CCCCCC'
                self.updateGraph(0)

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
                        day, departureTime), Timestamp(Timestamp.restoreDay(arrival), arrivalTime), flightNumber)
                    # self.flights.append(flight)
                    self.cities[sourceCity].addFlight(flight)

    def getCities(self):
        return self.cities
