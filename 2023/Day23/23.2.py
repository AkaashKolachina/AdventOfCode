import sys
from collections import deque
import time

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]
start = (0,grid[0].index('.'))
end = (len(grid) - 1, grid[-1].index('.'))

LEFT = (0,-1)
RIGHT = (0,1)
UP = (-1,0)
DOWN = (1,0)
dirs = [LEFT, RIGHT, UP, DOWN]
slopes = {">": RIGHT, "<": LEFT, "^":UP, "v":DOWN}

def get_neighbors(i,j):
    neighbors = []
    for di,dj in dirs:
        neighbors.append((i + di, j + dj))  

    neighbors = [(i,j) for (i,j) in neighbors if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != '#']
    return neighbors  

def get_neighbors_bfs(pos):
    neighbors = []
    visited = {pos}
    q = deque([(pos, 0)])
    while q:
        (i,j),d = q.pop()
        if (i,j) in junctions and (i,j) != pos:
            neighbors.append(((i,j), d))
        else:
            nbs = get_neighbors(i,j)
            for nb in nbs:
                if nb not in visited:
                    q.append((nb, d + 1))
                    visited.add(nb)
    return neighbors

junctions = {start:{}, end:{}}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '#' and len(get_neighbors(i,j)) > 2:
            junctions[(i,j)] = []

for jc in junctions:
    junctions[jc] = get_neighbors_bfs(jc)

start_time = time.time()
max_steps = 0
stack = [(start, 0, set())]
while stack:
    pos,num_steps,visited = stack.pop()
    if pos == end:
        max_steps = max(max_steps, num_steps)
    else:
        for nb,dist in junctions[pos]:
            if nb not in visited:
                stack.append((nb, num_steps + dist, visited | {nb}))

print(max_steps)
print(f'Time to brute force collapsed graph is {(time.time() - start_time)} seconds')