import sys
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

regions = set()
visited = set()
def get_neighbors(i,j):
    nbs = []
    dirs = [(0,1), (1,0), (-1,0), (0,-1)]
    for di,dj in dirs:
        if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
            nbs.append((i+di,j+dj))
    return nbs

def bfs(i,j):
    region = set()
    q = deque([(i,j)])
    while len(q):
        i,j = q.pop()
        region.add((i,j))

        for nb in get_neighbors(i,j):
            if nb not in visited and grid[nb[0]][nb[1]] == grid[i][j]:
                q.appendleft(nb)
                visited.add(nb)
    return frozenset(region)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in visited:
            visited.add((i,j))
            regions.add(bfs(i,j))

price = 0
for region in regions:
    area = len(region)
    num_corners = 0
    for i,j in region:
        if ((i, j+1) not in region and (i-1,j) not in region) or ((i, j+1) in region and (i-1,j) in region and (i-1,j+1) not in region):
            num_corners += 1
        if ((i, j-1) not in region and (i-1,j) not in region) or ((i, j-1) in region and (i-1,j) in region and (i-1,j-1) not in region):
            num_corners += 1
        if ((i, j-1) not in region and (i+1,j) not in region) or ((i, j-1) in region and (i+1,j) in region and (i+1,j-1) not in region):
            num_corners += 1
        if ((i, j+1) not in region and (i+1,j) not in region) or ((i, j+1) in region and (i+1,j) in region and (i+1,j+1) not in region):
            num_corners += 1
    price += (area*num_corners)
print(price)



