import sys
import networkx as nx

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

G = nx.Graph()

for line in lines:
    n1, rest = line.split(':')
    for n2 in rest.strip().split():
        G.add_edge(n1,n2)

to_cut = nx.minimum_edge_cut(G)

for u,v in to_cut:
    G.remove_edge(u,v)

parts = list(nx.connected_components(G))
print(len(parts[0]) * len(parts[1]))