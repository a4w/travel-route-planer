from Node import Node
from GraphAlgorithms import GraphAlgorithms


def printPath(parent, end):
    if(end in parent):
        printPath(parent, parent[end])
        print(str(parent[end].value) + '->' + str(end.value))


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.addEdge(n2, 1)
n1.addEdge(n4, 20)
n2.addEdge(n3, 1)
n3.addEdge(n4, 1)

parent = GraphAlgorithms.dijsktra(n1, n4)
printPath(parent, n4)
