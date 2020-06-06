from Node import Node
import math


class CartesianNode(Node):
    def __init__(self, value, x, y):
        super().__init__(value)
        self.x = x
        self.y = y

    def distanceTo(self, node):
        return CartesianNode.distance(self, node)

    def __hash__(self):
        return math.floor(self.x + self.y)

    @staticmethod
    def distance(u, v):
        return math.sqrt((u.x - v.x)**2 + (u.y - v.y)**2)

