import networkx as nx
import matplotlib.pyplot as plt
import time


class Visualizer:
    NODE_COLOR = '#333333'
    AVAILABLE_COLOR = '#CCCCCC'
    VISITED_COLOR = '#045582'
    FOUND_COLOR = '#009900'

    def __init__(self, cities, draw=True):
        self.cities = cities
        self.graph = nx.Graph()
        self.draw = draw
        for city in cities:
            city = cities[city]
            self.graph.add_node(city.name, pos=(city.latitude, city.longitude))
            self.graph.nodes[city.name]["node_color"] = self.NODE_COLOR
            self.update(0)

    def update(self, wait=0.5):
        if(not self.draw):
            return
        time.sleep(wait)
        plt.clf()
        colors = [self.graph.nodes[name]["node_color"]
                  for name in self.graph.nodes()]
        pos = nx.get_node_attributes(self.graph, 'pos')
        nx.draw_networkx(self.graph, with_labels=True,
                         node_color=colors, pos=pos)
        plt.draw()
        plt.pause(0.01)

    def reset(self):
        for n in self.graph.nodes():
            self.graph.nodes[n]["node_color"] = self.NODE_COLOR
        self.update()

    def visit(self, city, end=False):
        if(end):
            self.graph.nodes[city]["node_color"] = self.FOUND_COLOR
        else:
            self.graph.nodes[city]["node_color"] = self.VISITED_COLOR

        self.update()

    def markAvailable(self, city):
        self.graph.nodes[city]["node_color"] = self.AVAILABLE_COLOR
        self.update()

    def closeVisualizer(self):
        plt.close()
