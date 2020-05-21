from Node import Node
from CartesianNode import CartesianNode
from queue import PriorityQueue


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
