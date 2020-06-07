from CartesianNode import CartesianNode
from GraphAlgorithms import GraphAlgorithms
from FlightKnowledgeExtractor import FlightKnowledgeExtractor


def calculateDuration(source: dict, destination: dict):
    time = 0
    DAY_COST = 24 * 60  # Number of minutes in one day
    if(source["day"] <= destination["day"]):
        time = (destination["day"] - source["day"]) * DAY_COST
    else:
        time = (7 - (source["day"] - destination["day"])) * DAY_COST
    time = time + destination["time"]
    time = time - source["time"]
    return time


def normalizeDay(day: str):
    mapping = {
        "sun": 0,
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6
    }
    return mapping[day.lower()]


def isWithinDay(subject, start, end):
    if(start <= end):
        return subject >= start and subject <= end
    else:
        return subject <= start and subject >= end


def normalizeClock(clock: str):
    clock = clock.split(":")
    hour = int(clock[0])
    minutes = int(clock[1])
    return hour * 60 + minutes


def printPath(parent, end):
    if(end in parent):
        printPath(parent, parent[end])
        print(str(parent[end].value) + '->' + str(end.value))


n1 = CartesianNode(1, 0, 0)
n2 = CartesianNode(2, 1, 1)
n3 = CartesianNode(3, 2, 2)
n4 = CartesianNode(4, 2, 0)

n1.addEdge(n2, 10)
n1.addEdge(n4, 30)
n2.addEdge(n3, 10)
n3.addEdge(n4, 10)

parent = GraphAlgorithms.aStar(n1, n4)

kb = FlightKnowledgeExtractor(
    "./knowledge/cities.csv", "./knowledge/timetable.csv")

# Calculate speed of fastest plane
maxSpeed = 0
for src in kb.timetable:
    for trip in kb.timetable[src]:
        departure_days = str(trip[4]).strip("[]").split(",")
        for day in departure_days:
            day = day.strip()
            u = CartesianNode(
                {
                    "city": None,
                    "time": normalizeClock(trip[1]),
                    "day": normalizeDay(day)
                }, float(kb.cities[src]["x"]), float(kb.cities[src]["y"]))
            arrival_day = normalizeDay(day)
            if(normalizeClock(trip[2]) < normalizeClock(trip[1])):
                arrival_day = (arrival_day + 1) % 7
            v = CartesianNode(
                {
                    "city": None,
                    "time": normalizeClock(trip[2]),
                    "day": arrival_day
                }, float(kb.cities[trip[0]]["x"]), float(kb.cities[trip[0]]["y"]))
            duration = calculateDuration(u.value, v.value)
            distance = u.distanceTo(v) * 1000
            speed = distance / duration
            maxSpeed = max(maxSpeed, speed)

        # Assume we are going from Alexandria to London
from_city = "Aswan"
to_city = "London"
time_interval = [normalizeDay("sun"), normalizeDay("tue")]

# Create all available start nodes
departures = kb.timetable[from_city]

node = CartesianNode(
    {
        "city": from_city,
        "time": 0,
        "day": time_interval[0]
    }, float(kb.cities[from_city]["x"]), float(kb.cities[from_city]["y"]))

parent = GraphAlgorithms.exploringAStar(
    node, to_city, time_interval[1], kb, speed)

printPath(parent[0], parent[1])

