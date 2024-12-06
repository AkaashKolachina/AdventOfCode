import sys

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
dir_idx = 0

pos = start
steps = set()
while True:
    steps.add(pos)
    i2 = pos[0] + dirs[dir_idx][0]
    j2 = pos[1] + dirs[dir_idx][1]
    if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]):
        if grid[i2][j2] == '#':
            dir_idx = (dir_idx + 1) % 4
        else:
            steps.add(pos)
            pos = (i2,j2)
    else:
        break
print(len(steps))
