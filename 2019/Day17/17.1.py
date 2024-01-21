import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

ic = IntCode(program.copy())
grid = [[]]

has_halted = False
while not has_halted:
    output = ic.run()
    if output is None:
        has_halted = True
        break
    if output == 10:
        grid.append([])
    else:
        grid[-1].append(chr(output))

grid = grid[:grid.index([])]
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
align_param_sum = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        nbs = []
        for dir in dirs:
            nbs.append((i + dir[0], j + dir[1]))
        nbs = [nb for nb in nbs if 0 <= nb[0] < len(grid) and 0 <= nb[1] < len(grid[0])]
        if grid[i][j] == '#' and len(nbs) == 4 and all(grid[i2][j2] == '#' for (i2,j2) in nbs):
            align_param_sum += i*j

print(align_param_sum)
