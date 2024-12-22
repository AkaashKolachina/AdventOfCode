import sys
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]


S = (-1,-1)
E = (-1,-1)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            S = (i,j)
        elif grid[i][j] == 'E':
            E = (i,j)

def get_nbs(i,j):
    nbs = []
    dirs = [(0,1),(1,0), (0,-1), (-1,0)]
    for di,dj in dirs:
        if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i+di][j+dj] != '#':
            nbs.append((i+di,j+dj))
    return nbs

q = deque([(S,0)])
dist_to = {}
while len(q):
    point,dist = q.pop()
    if point not in dist_to:
        dist_to[point] = dist
    else:
        continue
    
    i,j = point
    for nb in get_nbs(i,j):
        q.appendleft((nb,dist + 1))

dist_from = {}
q = deque([(E,0)])
while len(q):
    point,dist = q.pop()
    if point not in dist_from:
        dist_from[point] = dist
    else:
        continue
    
    i,j = point
    for nb in get_nbs(i,j):
        q.appendleft((nb,dist + 1))

count = 0
for i,j in dist_to:
    cands = []
    for di in range(-2,3):
        for dj in range(-2 + abs(di), 2 - abs(di) + 1):
            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i+di][j+dj] != '#' and (i+di,j+dj) in dist_from:
                cands.append((i+di,j+dj))
    for cand in cands:
        if dist_to[E] - (dist_to[(i,j)] + dist_from[cand] + sum(abs(p1 - p2) for p1, p2 in zip((i,j), cand))) >= 100:
            count += 1

print(count)