import sys
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

start = None
start_found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i,j)
            start_found = True
            break
    if start_found:
        break

def get_neighbors(i,j):
    neighbors = []
    for di,dj in dirs:
        neighbors.append((i + di, j + dj))
    neighbors = [(i2,j2) for (i2,j2) in neighbors if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] != '#']
    return neighbors

visited = set()
q = deque([(start,0)])
num_steps = 0
max_steps = 64
last_step = set()
while q:
    entry = q.pop()
    (i,j), num_steps = entry
    if entry in visited:
        continue
    visited.add(entry)
    for nb in get_neighbors(i,j):
        if num_steps == max_steps - 1:
            last_step.add(nb)
        q.appendleft((nb, num_steps + 1))
    if num_steps == max_steps:
        print(len(last_step))
        break