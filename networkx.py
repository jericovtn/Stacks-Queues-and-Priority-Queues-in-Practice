import networkx as nx

graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]

print(nx.nx_agraph.read_dot("roadmap.dot"))
    