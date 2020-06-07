from Node import Node
from CartesianNode import CartesianNode
from queue import PriorityQueue
from queue import Queue


def calculateDuration(source: dict, destination: dict) -> int:
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


class GraphAlgorithms():

    @staticmethod
    def dijsktra(startNode: Node, endNode: Node) -> dict:
        upcoming = PriorityQueue()
        # We add a tuple, first element is the cost, the second is the node
        upcoming.put((0, startNode))

        # To store path to source
        parent = dict()

        # To store minimum cost from startNode to a given node
        costs = dict()
        costs[startNode] = 0

        while not upcoming.empty():
            current: Node = upcoming.get()[1]

            # Check if we found the destination
            if(current == endNode):
                return parent

            for adj in current.neighbours:
                # Adjacent node
                node: Node = adj[0]
                # Edge cost
                cost: int = adj[1]

                # New cost to neighbour
                newCost: int = costs[current] + cost

                if(node not in costs or newCost < costs[node]):
                    parent[node] = current
                    costs[node] = newCost
                    upcoming.put((newCost, node))

        # No path found
        raise Exception("No path between source and destination found")

    @staticmethod
    def aStar(startNode: CartesianNode, endNode: CartesianNode):
        upcoming = PriorityQueue()
        # We add a tuple, first element is the cost, the second is the node
        upcoming.put((0, startNode))

        # To store path to source
        parent = dict()

        # To store minimum cost from startNode to a given node
        costs = dict()
        costs[startNode] = 0

        while not upcoming.empty():
            current: CartesianNode = upcoming.get()[1]

            # Check if we found the destination
            if(current == endNode):
                return parent

            for adj in current.neighbours:
                # Adjacent node
                node: CartesianNode = adj[0]
                # Edge cost
                cost: int = adj[1]

                # New cost to neighbour
                newCost: int = costs[current] + cost

                if(node not in costs or newCost < costs[node]):
                    parent[node] = current
                    costs[node] = newCost
                    # Add the heuristic cost
                    newCost = newCost + node.distanceTo(endNode)
                    upcoming.put((newCost, node))

        # No path found
        raise Exception("No path between source and destination found")

    @staticmethod
    def exploringAStar(startNode: CartesianNode, to_city: str, end_day: int, knowledge, speed):
        upcoming = PriorityQueue()
        # We add a tuple, first element is the cost, the second is the node
        upcoming.put((0, startNode))

        # To store path to source
        parent = dict()

        # To store minimum cost from startNode to a given node
        costs = dict()
        costs[startNode] = 0

        while not upcoming.empty():
            current: CartesianNode = upcoming.get()[1]

            # Check if we found the destination
            if(current.value["city"] == to_city):
                return (parent, current)

            # Prepare neighbours
            nextMoves = knowledge.timetable[current.value["city"]]
            print(current.value["city"])
            for move in nextMoves:
                print(move)
                departure_days = str(move[4]).strip("[]").split(",")
                for day in departure_days:
                    day = day.strip()
                    normalizedDay = normalizeDay(day)
                    if(isWithinDay(normalizedDay, current.value["day"], end_day)):
                        # Check time as well
                        if(normalizedDay == current.value["day"] and normalizeClock(move[1]) < current.value["time"]):
                            continue

                        # Ok add as neighbour
                        arrival_day = normalizedDay
                        if(normalizeClock(move[2]) < normalizeClock(move[1])):
                            arrival_day = (arrival_day + 1) % 7
                        node = CartesianNode(
                            {
                                "city": move[0],
                                "time": normalizeClock(move[2]),
                                "day": arrival_day
                            }, float(knowledge.cities[move[0]]["x"]), float(knowledge.cities[move[0]]["y"]))
                        current.neighbours.append(
                            (node, calculateDuration(current.value, node.value)))

            for adj in current.neighbours:
                # Adjacent node
                node: CartesianNode = adj[0]
                # Edge cost
                cost: int = adj[1]

                # New cost to neighbour
                newCost: int = costs[current] + cost

                print("Cost from " + str(current.value["city"]) + " at " + str(node.value["day"]) + " " + str(node.value["time"]) + " to " + str(
                    node.value["city"]) + " is " + str(newCost))

                if(node not in costs or newCost < costs[node]):
                    parent[node] = current
                    costs[node] = newCost
                    # Add the heuristic cost
                    endNode = CartesianNode(
                        None, knowledge.cities[to_city]["x"], knowledge.cities[to_city]["y"])
                    # Since we work with times, we need to convert distance to time
                    newCost = newCost + node.distanceTo(endNode) / speed
                    # Calculate heuristic
                    upcoming.put((newCost, node))

        # No path found
        raise Exception("No path between source and destination found")
