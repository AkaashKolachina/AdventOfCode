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

visited = set([(S,0)])
q = []
heappush(q,(0,S,0))
while len(q):
    cur_score,(i,j),dir_idx = heappop(q)
    if (i,j) == E:
        print(cur_score)
        break
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
