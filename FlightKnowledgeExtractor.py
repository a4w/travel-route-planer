import csv
from collections import defaultdict


class FlightKnowledgeExtractor:
    def __init__(self, citiesFile, timetableFile):
        # Read cities and save them in list
        self.cities = dict()
        with open(citiesFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.cities[row[0]] = {"x": row[1], "y": row[2]}

        self.timetable = defaultdict(list)
        with open(timetableFile) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.timetable[row[0]].append(row[1:])

