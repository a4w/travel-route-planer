from FlightKnowledgeExtractor import FlightKnowledgeExtractor
from TravelRoutePlanner import TravelRoutePlanner

kb = FlightKnowledgeExtractor(
    "./knowledge/cities.csv", "./knowledge/timetable.csv")
cities = kb.getCities()

# Inputs
from_city = str(input("Source city: "))
to_city = str(input("Destination city: "))
start_time = str(input("Start day: "))
end_time = str(input("End day: "))

planner = TravelRoutePlanner(kb, from_city, to_city, start_time, end_time)
for i in range(7):
    try:
        planner.printOptimalPath()
        break
    except:
        print("No route found in range, increasing start and end dates")
        planner.widenRange()

