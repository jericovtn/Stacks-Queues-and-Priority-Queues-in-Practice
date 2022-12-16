# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 2. Using Queues in Practice
# December 17, 2022

# 1
from typing import NamedTuple
import networkx as nx

# 2
from queues import Queue

# 1: Object Representation of the Cities and Roads
# Implemented Class City
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )

# Added the following helper function to graph module
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )

# 2: Breadth-First Search Using a FIFO Queue
# Extract logic into a separate function 

# Modified
def breadth_first_traverse(graph, source, order_by=None):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        # Added
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

# Modified
def breadth_first_search(graph, source, predicate, order_by=None):
    for node in breadth_first_traverse(graph, source, order_by):
        if predicate(node):
            return node

# 3: Shortest Path Using Breadth-First Traversal
# Copying and adapting the code from your earlier breadth_first_traverse() function
def shortest_path(graph, source, destination, order_by=None):
    queue = Queue(source)
    visited = {source}
    previous = {}
    while queue:
        node = queue.dequeue()
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous[neighbor] = node
                if neighbor == destination:
                    return retrace(previous, source, destination)