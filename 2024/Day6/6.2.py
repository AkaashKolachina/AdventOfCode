import sys
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

start = (-1,-1)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            start = (i,j)
            break

dirs = [(-1,0), (0,1), (1,0), (0,-1)]
num_opts = 0
for i in tqdm(range(len(grid))):
    for j in range(len(grid[0])):
        if (i,j) != start and grid[i][j] != '#':
            found_loop = False
            dir_idx = 0
            steps = set()
            pos = start
            while not found_loop:
                steps.add((pos,dir_idx))
                i2 = pos[0] + dirs[dir_idx][0]
                j2 = pos[1] + dirs[dir_idx][1]
                if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]):
                    if ((i2,j2),dir_idx) in steps:
                        num_opts += 1
                        found_loop = True
                        break

                    if grid[i2][j2] == '#' or (i2 == i and j2 == j):
                        dir_idx = (dir_idx + 1) % 4
                    else:
                        pos = (i2,j2)
                else:
                    break
print(num_opts)