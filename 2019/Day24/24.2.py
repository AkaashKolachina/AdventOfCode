import sys
from copy import deepcopy
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

BUG = '#'
EMPTY = '.'
mid = (2,2)
empty_grid = [['.' for j in range(5)] for i in range(5)]
grids = defaultdict(lambda : (deepcopy(empty_grid), 0))
grids[0] = (grid, sum(row.count(BUG) for row in grid))

def get_neighbors(pos, level):
    i,j = pos
    dirs = [(0,-1), (0,1), (1,0), (-1,0)]
    nbs = []
    for dir in dirs:
        nbs.append((i + dir[0], j + dir[1]))
    nbs = [grids[level][0][i2][j2] for (i2,j2) in nbs if 0 <= i2 < 5 and 0 <= j2 < 5 and (i2,j2) != mid]

    if j == 4:
        nbs.append(grids[level + 1][0][2][3])
    if j == 0:
        nbs.append(grids[level + 1][0][2][1])
    if i == 4:
        nbs.append(grids[level + 1][0][3][2])
    if i == 0:
        nbs.append(grids[level + 1][0][1][2])

    if pos == (1,2):
        for j2 in range(5):
            nbs.append(grids[level - 1][0][0][j2])
    if pos == (3,2):
        for j2 in range(5):
            nbs.append(grids[level - 1][0][4][j2])
    if pos == (2,1):
        for i2 in range(5):
            nbs.append(grids[level - 1][0][i2][0])
    if pos == (2,3):
        for i2 in range(5):
            nbs.append(grids[level - 1][0][i2][4])

    return nbs

min_level = -1
max_level = 1
for _ in range(200):
    temp = {}
    for level in range(min_level, max_level + 1):
        next_grid, num_bugs = deepcopy(grids[level])
        for i in range(5):
            for j in range(5):
                if (i,j) == mid:
                    continue
                nbs = get_neighbors((i,j), level)
                if grids[level][0][i][j] == BUG:
                    if nbs.count(BUG) != 1:
                        next_grid[i][j] = EMPTY
                        num_bugs -= 1
                else:
                    bug_count = nbs.count(BUG)
                    if bug_count ==  1 or bug_count == 2:
                        next_grid[i][j] = BUG
                        num_bugs += 1
        temp[level] = (next_grid, num_bugs)

    for key in temp:
        grids[key] = temp[key]

    if grids[min_level][1] > 0:
        min_level -= 1
    if grids[max_level][1] > 0:
        max_level += 1

total_bugs = sum(num_bugs for _,num_bugs in grids.values())
print(total_bugs)