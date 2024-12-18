import sys
from heapq import *

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x.split(',') for x in data.split('\n')]
for i in range(len(lines)):
    lines[i] = (int(lines[i][0]), int(lines[i][1]))

NUM_ROWS = 71
NUM_COLS = 71
E = (70,70)
NUM_FALLS = 1024

def get_neighbors(i,j):
    nbs = []
    dirs = [(0,1),(0,-1),(1,0), (-1,0)]
    for di,dj in dirs:
        if 0 <= i + di < NUM_ROWS and 0 <= j + dj < NUM_COLS:
            nbs.append((i+di,j+dj))
    return nbs

corrupted = set(lines[:NUM_FALLS])

q = [(0,(0,0))]
visited = set((0,0))

while len(q):
    dist,(i,j)= heappop(q)
    if (i,j) == E:
        print(dist)
        break

    nbs = get_neighbors(i,j)
    for nb in nbs:
        if nb not in corrupted and nb not in visited:
            heappush(q,(dist+1,nb))
            visited.add(nb)

