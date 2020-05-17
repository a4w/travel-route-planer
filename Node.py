class Node():
    def __init__(self, value):
        self.value = value
        self.neighbours = list()

    def addEdge(self, node, cost):
        self.neighbours.append((node, cost))
        node.neighbours.append((self, cost))

    def addDirectedEdge(self, node, cost):
        self.neighbours.append((node, cost))

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value
