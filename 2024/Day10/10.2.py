import sys
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [[int(num) for num in x] for x in data.split('\n')]

def get_neighbors(i,j):
    dirs = [(0,1), (1,0),(-1,0),(0,-1)]
    nbs = []
    for di,dj in dirs:
        if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
            nbs.append((i+di,j+dj))
    return nbs

def bfs(i,j):
    num_paths = 0
    visited = set(((i,j), frozenset((i,j))))
    q = deque([((i,j),set((i,j)))])
    while len(q):
        (i,j),path = q.pop()
        if grid[i][j] == 9:
            num_paths += 1

        nbs = get_neighbors(i,j)
        for nb in nbs:
            if (nb,frozenset(path | {nb})) not in visited and (grid[nb[0]][nb[1]] - grid[i][j]) == 1:
                visited.add(nb)
                q.appendleft((nb,path | {nb}) )
    
    return num_paths

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            total += bfs(i,j)
print(total)

