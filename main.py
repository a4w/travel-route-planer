from FlightKnowledgeExtractor import FlightKnowledgeExtractor
from TravelRoutePlanner import TravelRoutePlanner


def isWithinDay(subject, start, end):
    if(start <= end):
        return subject >= start and subject <= end
    else:
        return subject <= start and subject >= end


def printPath(parent, end):
    if(end in parent):
        printPath(parent, parent[end])
        print(str(parent[end].value) + '->' + str(end.value))


kb = FlightKnowledgeExtractor(
    "./knowledge/cities.csv", "./knowledge/timetable.csv")
cities = kb.getCities()

# Inputs
from_city = "Aswan"
to_city = "London"
start_time = "sun"
end_time = "sun"

planner = TravelRoutePlanner(kb, from_city, to_city, start_time, end_time)
for i in range(7):
    try:
        planner.printOptimalPath()
        break
    except:
        print("No route found in range, increasing start and end dates")
        planner.widenRange()

