from Node import Node
from CartesianNode import CartesianNode
from queue import PriorityQueue


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
    def exploringAStar(startNode: CartesianNode, to_city: str, end_day: int, knowledge):
        upcoming = PriorityQueue()
        # We add a tuple, first element is the cost, the second is the node
        upcoming.put((0, startNode))

        # To store path to source
        parent = dict()

        # To store minimum cost from startNode to a given node
        costs = dict()
        costs[startNode] = 0

        currentTime = startNode.value["time"]

        while not upcoming.empty():
            current: CartesianNode = upcoming.get()[1]

            # Check if we found the destination
            if(current.value["city"] == to_city):
                return parent

            # Prepare neighbours
            nextMoves = knowledge.timetable[current.value["city"]]
            for move in nextMoves:
                departure_days = str(move[4]).strip("[]").split(",")
                for day in departure_days:
                    day = day.strip()
                    normalizedDay = normalizeDay(day)
                    if(isWithinDay(normalizedDay, current.value["day"], end_day)):
                        # Ok add as neighbour
                        node = CartesianNode(
                            {
                                "city": move[0],
                                "time": move[2],
                                "day": normalizedDay
                            }, float(knowledge.cities[move[0]]["x"]), float(knowledge.cities[move[0]]["y"]))
                        print(node.value)

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
