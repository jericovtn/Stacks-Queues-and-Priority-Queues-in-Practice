import networkx as nx
from graph import City, load_graph

def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")

graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]

nodes, graph = load_graph("roadmap.dot", City.from_dict)
nodes["london"]

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
    
def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")
    
print(nx.nx_agraph.read_dot("roadmap.dot"))
print(graph)