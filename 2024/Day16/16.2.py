import sys
from heapq import *

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

S = (-1,-1)
E = (-1,-1)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            S = (i,j)
        elif grid[i][j] == 'E':
            E = (i,j)

best_score = None
dist_to = {}
visited = set([(S,0)])
q = []
heappush(q,(0,S,0))
while len(q):
    cur_score,(i,j),dir_idx = heappop(q)
    if ((i,j),dir_idx) not in dist_to:
        dist_to[((i,j),dir_idx)] = cur_score
    if (i,j) == E:
        if not best_score:
            best_score = cur_score
    for inc in [1,-1]:
        new_dir = (dir_idx + inc) % len(dirs)
        if ((i,j),new_dir) not in visited:
            visited.add(((i,j),new_dir))
            heappush(q,(cur_score + 1000, (i,j), new_dir))
    i2 = i + dirs[dir_idx][0]
    j2 = j + dirs[dir_idx][1]
    if grid[i2][j2] != '#' and ((i2,j2),dir_idx) not in visited:
        visited.add(((i2,j2),dir_idx))
        heappush(q,(cur_score + 1, (i2,j2), dir_idx))

dist_from = {}
q = []
visited = set()
for i in range(4):
    visited.add((E,i))
    heappush(q,(0,E,i))
while len(q):
    cur_score,(i,j),dir_idx = heappop(q)
    if ((i,j),dir_idx) not in dist_from:
        dist_from[((i,j),dir_idx)] = cur_score
    
    for inc in [1,-1]:
        new_dir = (dir_idx + inc) % len(dirs)
        if ((i,j),new_dir) not in visited:
            visited.add(((i,j),new_dir))
            heappush(q,(cur_score + 1000, (i,j), new_dir))

    back_dir = (dir_idx + 2) % len(dirs)
    i2 = i + dirs[back_dir][0]
    j2 = j + dirs[back_dir][1]
    if grid[i2][j2] != '#' and ((i2,j2),dir_idx) not in visited:
        heappush(q,(cur_score + 1, (i2,j2), dir_idx))

tiles = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        for dir_idx in range(len(dirs)):
            tile = ((i,j),dir_idx)
            if tile in dist_to and tile in dist_from and dist_to[tile] + dist_from[tile] == best_score:
                tiles.add(tile[0])

print(len(tiles))