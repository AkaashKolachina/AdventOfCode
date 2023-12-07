from sys import argv
from collections import defaultdict, deque
import networkx as nx

data = open(argv[1]).read().strip()
lines = [x for x in data.split('\n')]

flows = defaultdict(int)
paths = defaultdict(list)
valves = []
max_paths = defaultdict(int)
for line in lines:
    parts = line.split(' ')
    valve = parts[1]
    f_rate = parts[4].split('=')[1]
    flows[valve] = int(f_rate[:-1])
    valve_paths = ''.join(parts[9:]).split(',')
    paths[valve] = valve_paths
    if flows[valve] > 0:
        valves.append(valve)

G = nx.Graph()
for node_1 in paths:
    for node_2 in paths[node_1]:
        G.add_edge(node_1, node_2)
dists = nx.floyd_warshall(G)

def bfs():
    q = deque()
    visited = set()
    # (node, time_left, total_relief, visited_valves)
    start = ('AA', 30, 0, frozenset(set()))
    q.append(start)
    visited.add(start)

    while len(q) > 0:
        node = q.popleft()
        #print(node)
        (node_val, time, relief, vis_valves) = node
        for valve in valves:
            if valve == node_val or valve in vis_valves:
                continue

            # get time to valve
            d = int(dists[node_val][valve])
            new_time = time - (1+d)
            new_relief = relief + (new_time * flows[valve])
            vis_s = set(vis_valves)
            vis_s.add(valve)
            frozen = frozenset(vis_s)
            entry = (valve, new_time, new_relief, frozen)
            if entry in visited:
                continue
            if time < 0:
                continue
            q.append(entry)
            max_paths[frozen] = max(max_paths[frozen], entry[2])

bfs()
print(max(max_paths.values()))