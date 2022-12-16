import networkx as nx
from graph import City, load_graph
from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,)
from graph import shortest_path
from graph import connected

# Variables
graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]

nodes, graph = load_graph("roadmap.dot", City.from_dict)
nodes["london"]

city1 = nodes["aberdeen"]
city2 = nodes["perth"]


# Def
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name

" → ".join(city.name for city in shortest_path(graph, city1, city2))


def by_latitude(city):
    return -city.latitude

" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
)

# For
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))

for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")

for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)

for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)

for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")
    
for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")

print(nx.nx_agraph.read_dot("roadmap.dot"))
print(graph)

connected(graph, nodes["belfast"], nodes["glasgow"])
connected(graph, nodes["belfast"], nodes["derry"])
