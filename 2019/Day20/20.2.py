import sys
from collections import defaultdict,deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

pad_len = len(grid[1]) - len(grid[0])
grid[0] = [' ' for _ in range(pad_len)] + grid[0]
start = None
end = None

first_row = 2
last_row = len(grid) - 3
first_col = 2
last_col = len(grid[0]) - 3

void_first_row = None
void_last_row = None
void_first_col = None
void_last_col = None

found_void = False
row = first_row
while not found_void:
    if ' ' in grid[row][first_col:last_col + 1]:
        found_void = True
        void_first_row = row
        col_idxs = [i for i in range(first_col, last_col + 1) if grid[row][i].isnumeric() or grid[row][i] == ' ']
        void_first_col = min(col_idxs)
        void_last_col = max(col_idxs)
    else:
        row += 1

found_void = False
row = last_row
while not found_void:
    if ' ' in grid[row][first_col: last_col + 1]:
        found_void = True
        void_last_row = row
    else:
        row -= 1

warp_points = defaultdict(list)

#TODO: atleast abstract some of this into functions
inners = set()
outers = set()
sets = [outers, inners]
col_bounds = [(first_col,last_col), (void_first_col, void_last_col)]
for idx,i in enumerate([first_row, void_last_row + 1]):
    for j in range(col_bounds[idx][0], col_bounds[idx][1] + 1):
        if grid[i][j] == '.':
            name = grid[i-2][j] + grid[i-1][j]
            if name == 'AA':
                start = (i,j)
            elif name == 'ZZ':
                end = (i,j)
            else:
                warp_points[name].append((i,j))
                sets[idx].add((i,j))

for idx,i in enumerate([last_row, void_first_row - 1]):
    for j in range(col_bounds[idx][0], col_bounds[idx][1] + 1):
        if grid[i][j] == '.':
            name = grid[i+1][j] + grid[i+2][j]
            if name == 'AA':
                start = (i,j)
            elif name == 'ZZ':
                end = (i,j)
            else:
                warp_points[name].append((i,j))
                sets[idx].add((i,j))

row_bounds = [(first_row, last_row), (void_first_row, void_last_row)]
for idx,j in enumerate([first_col, void_last_col + 1]):
    for i in range(row_bounds[idx][0], row_bounds[idx][1] + 1):
        if grid[i][j] == '.':
            name = grid[i][j-2] + grid[i][j-1]
            if name == 'AA':
                start = (i,j)
            elif name == 'ZZ':
                end = (i,j)
            else:
                warp_points[name].append((i,j))
                sets[idx].add((i,j))

for idx,j in enumerate([last_col, void_first_col - 1]):
    for i in range(row_bounds[idx][0], row_bounds[idx][1] + 1):
        if grid[i][j] == '.':
            name = grid[i][j+1] + grid[i][j+2]
            if name == 'AA':
                start = (i,j)
            elif name == 'ZZ':
                end = (i,j)
            else:
                warp_points[name].append((i,j))
                sets[idx].add((i,j))

warps = {}
for name in warp_points:
    p1,p2 = warp_points[name]
    warps[p1] = p2
    warps[p2] = p1

def get_neighbors(pos):
    pos,level = pos
    i,j = pos
    dirs = [(0,-1), (0,1), (1,0), (-1,0)]
    nbs = []
    for dir in dirs:
        nbs.append((i + dir[0], j + dir[1]))
    nbs = [((i2,j2),level) for (i2,j2) in nbs if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] == '.' ]
    if level == 0:
        nbs = [nb for nb in nbs if nb not in outers]
    if level != 0:
        nbs = [nb for nb in nbs if nb not in [start,end]]
    if pos in inners:
        nbs.append((warps[pos], level + 1))
    if pos in outers and level != 0:
        nbs.append((warps[pos], level - 1))
    return nbs

visited = set()
q = deque([((start,0),0)])

while q:
    pos, steps = q.pop()
    if pos in visited:
        continue
    visited.add(pos)
    if pos == (end,0):
        print(steps)
        break
    
    nbs = get_neighbors(pos)
    for nb in nbs:
        q.appendleft((nb, steps + 1))

