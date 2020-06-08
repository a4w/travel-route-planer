from City import City
from Timestamp import Timestamp
from FlightKnowledgeExtractor import FlightKnowledgeExtractor
from Visualizer import Visualizer
from queue import PriorityQueue


class TravelRoutePlanner:
    def __init__(self, knowledge: FlightKnowledgeExtractor, fromCity, toCity, startDay, endDay, visualize=False):
        self.knowledge = knowledge
        self.cities = knowledge.getCities()
        self.fromCity = self.cities[fromCity]
        self.toCity = self.cities[toCity]
        self.startDay = Timestamp.normalizeDay(startDay)
        self.endDay = Timestamp.normalizeDay(endDay)
        self.visualizer = Visualizer(self.cities, visualize)

    def widenRange(self):
        self.startDay = Timestamp.prevDay(self.startDay)
        self.endDay = Timestamp.nextDay(self.endDay)

    def printOptimalPath(self):
        route = self._plan()
        for x in route:
            print(x)
        self.visualizer.freeze()

    def _plan(self) -> list:
        upcoming = PriorityQueue()

        self.visualizer.reset()

        # We add a tuple, first element is the cost, the second is the node
        upcoming.put((0, self.fromCity))

        # To store path to source
        path = dict()

        # To store minimum cost from startNode to a given node
        costs = dict()
        costs[self.fromCity] = 0
        timestamps = dict()
        timestamps[self.fromCity] = Timestamp(
            Timestamp.restoreDay(self.startDay), "00:00")
        maxTimestamp = Timestamp(
            Timestamp.restoreDay(self.endDay), "23:59")

        while not upcoming.empty():
            tu = upcoming.get()
            current: City = tu[1]
            self.visualizer.visit(current.name)

            # Check if we found the destination
            if(current == self.toCity):
                # Unroll parents
                route = list()
                city = self.toCity
                self.visualizer.visit(current.name, True)
                while(city in path):
                    flight = path[city][1]
                    route.append(flight)
                    city = path[city][0]
                route.reverse()
                return route

            flights = current.getFlights()
            for flight in flights:
                if(not Timestamp.within(flight.departure, timestamps[current], maxTimestamp)):
                    continue
                if(not Timestamp.within(flight.arrival, timestamps[current], maxTimestamp)):
                    continue

                # Edge cost
                cost: int = Timestamp.calculateDuration(
                    timestamps[current], flight.arrival)

                # New cost to neighbour
                newCost: int = costs[current] + cost

                if(flight.destinationCity not in costs or newCost < costs[flight.destinationCity]):
                    path[flight.destinationCity] = (current, flight)
                    costs[flight.destinationCity] = newCost
                    timestamps[flight.destinationCity] = flight.arrival
                    # Add the heuristic cost
                    newCost = newCost + \
                        current.distanceTo(flight.destinationCity)
                    # Calculate heuristic
                    upcoming.put((newCost, flight.destinationCity))
                    self.visualizer.markAvailable(
                        flight.destinationCity.name)

        # No path found
        raise Exception("No path between source and destination found")
