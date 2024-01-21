import sys
sys.path.append('..')
from intcode import IntCode
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

cur = [0,0]
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
deltas = {0: -1, 1: 1}
ic = IntCode(program.copy())
painted = defaultdict(int)
painted[(0,0)] = 1

dir_idx = 0
has_halted = False
while not has_halted:
    ic.add_input(painted[tuple(cur)])
    color = ic.run()
    if color is None:
        has_halted = True
        continue
    painted[tuple(cur)] = color

    turn = ic.run()
    if turn is None:
        has_halted = True
        continue
    dir_idx = (dir_idx+ deltas[turn]) % len(dirs)
    cur[0] += dirs[dir_idx][0]
    cur[1] += dirs[dir_idx][1]

mins = [float('inf'), float('inf')]
maxs = [-float('inf'), -float('inf')]
for i,j in painted:
    mins[0] = min(mins[0],i)
    mins[1] = min(mins[1],j)
    maxs[0] = max(maxs[0],i)
    maxs[1] = max(maxs[1],j)

plate = []
for i in range(mins[0], maxs[0] + 1):
    plate.append([])
    for j in range(mins[1], maxs[1] + 1):
        symbol = '#' if painted[(i,j)] else ' '
        plate[-1].append(symbol)

for line in plate:
    print(''.join(line))
