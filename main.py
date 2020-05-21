from CartesianNode import CartesianNode
from GraphAlgorithms import GraphAlgorithms


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
printPath(parent, n4)
