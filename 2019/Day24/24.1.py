import sys
from copy import deepcopy

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

BUG = '#'
EMPTY = '.'
def get_neighbors(pos):
    i,j = pos
    dirs = [(0,-1), (0,1), (1,0), (-1,0)]
    nbs = []
    for dir in dirs:
        nbs.append((i + dir[0], j + dir[1]))
    nbs = [grid[i2][j2] for (i2,j2) in nbs if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0])]
    return nbs

def freeze_grid():
    return tuple(tuple(row) for row in grid)

seen = set()
found_cycle = False
while not found_cycle:
    next_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            nbs = get_neighbors((i,j))
            if grid[i][j] == BUG:
                if nbs.count(BUG) != 1:
                    next_grid[i][j] = EMPTY
            else:
                num_bugs = nbs.count(BUG)
                if num_bugs ==  1 or num_bugs == 2:
                    next_grid[i][j] = BUG

    state = freeze_grid()
    if state in seen:
        found_cycle = True
    else:
        seen.add(state)
        grid = next_grid

bio_rating = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == BUG:
            bio_rating += pow(2,i*len(grid[0]) + j)
print(bio_rating)