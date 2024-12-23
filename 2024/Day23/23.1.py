import sys
import networkx as nx

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

G = nx.Graph()
nodes = set()
for line in lines:
    x,y = line.split('-')
    G.add_edge(x,y)
    if 't' in x:
        nodes.add(x)
    if 't' in y:
        nodes.add(y)

cliques = nx.enumerate_all_cliques(G)
triangles = [clique for clique in cliques if len(clique) == 3]
count = 0
for triangle in triangles:
    if any(node[0] == 't' for node in triangle):
        count += 1
print(count)
