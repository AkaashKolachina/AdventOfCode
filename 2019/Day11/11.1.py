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
print(len(painted))
