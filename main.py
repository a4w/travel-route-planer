from CartesianNode import CartesianNode
from GraphAlgorithms import GraphAlgorithms
from FlightKnowledgeExtractor import FlightKnowledgeExtractor


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


# Assume we are going from Alexandria to London
from_city = "Alexandria"
to_city = "London"
time_interval = [normalizeDay("sun"), normalizeDay("tue")]

# Create all available start nodes
departures = kb.timetable[from_city]

for trip in departures:
    # Check if time and day are within available range
    # Any time is ok in this problem
    departure_time = normalizeClock(trip[1])
    departure_days = str(trip[4]).strip("[]").split(",")
    for day in departure_days:
        day = day.strip()
        # Check if day is within travel range
        normalizedDay = normalizeDay(day)
        if(isWithinDay(normalizedDay, time_interval[0], time_interval[1])):
            # Create available start node
            print("Found " + day)

