import sys
from collections import defaultdict, deque
import heapq

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

start = None
keys = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            start = (i,j)
        if grid[i][j].islower():
            keys.add((i,j))

G = defaultdict(dict)

def get_neighbors(pos):
    i,j = pos
    dirs = [(0,-1), (0,1), (1,0), (-1,0)]
    nbs = []
    for dir in dirs:
        nbs.append((i + dir[0], j + dir[1]))
    nbs = [(i2,j2) for (i2,j2) in nbs if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] != '#']
    return nbs

def get_collapsed_neighbors(pos):
    visited = set()
    q = deque([(pos,0,set())])
    while q:
        p, num_steps, keys_needed = q.pop()
        i,j = p
        visited.add(p)

        if grid[i][j].isupper():
           keys_needed.add(grid[i][j].lower())

        if grid[i][j].islower() and (i,j) != pos: 
            G[grid[pos[0]][pos[1]]][grid[i][j]] = (num_steps, keys_needed)
            continue

        nbs = get_neighbors(p)
        for nb in nbs:
            if nb not in visited:
                q.appendleft((nb, num_steps + 1,  keys_needed.copy()))

si,sj = start
grid[si + 1][sj + 1] = '4'
grid[si - 1][sj + 1] = '2'
grid[si + 1][sj - 1] = '3'
grid[si - 1][sj - 1] = '1'
hashes = get_neighbors(start)
hashes.append(start)
for i,j in hashes:
    grid[i][j] = '#'
starts = [(si + 1, sj + 1), (si - 1, sj + 1),(si + 1, sj - 1),(si - 1, sj - 1)]

for s in starts:
    get_collapsed_neighbors(s)
for key in keys:
    get_collapsed_neighbors(key)

visited = set()
pq = [(0,['1','2','3','4'], set())]

while pq:
    steps, nodes, cur_keys = heapq.heappop(pq)
    cur_keys = set(cur_keys)
    for node in nodes:
        if not node.isnumeric():
            cur_keys.add(node)
    frozen_keys = frozenset(cur_keys)
    if (tuple(nodes), frozen_keys) in visited:
        continue
    visited.add((tuple(nodes), frozen_keys))
    if len(frozen_keys) == len(keys):
        print(steps)
        break

    for i,node in enumerate(nodes):
        for nb in G[node]:
            if frozen_keys.issuperset(G[node][nb][1]):
                next_nodes = nodes.copy()
                next_nodes[i] = nb
                heapq.heappush(pq,(steps + G[node][nb][0], next_nodes, frozen_keys))
