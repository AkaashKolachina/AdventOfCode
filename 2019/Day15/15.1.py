import sys
sys.path.append('..')
from intcode import IntCode
from copy import deepcopy
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
opposite = {NORTH : SOUTH, SOUTH : NORTH, EAST : WEST, WEST : EAST}
dirs = {NORTH : (-1,0), SOUTH : (1,0), EAST: (0,1), WEST: (0,-1)}

visited = set()
q = deque([(IntCode(program.copy()), (0,0), 0)])

while q:
    ic, (i,j), num_steps = q.pop()
    visited.add((i,j))

    for dir in dirs:
        clone = deepcopy(ic)
        clone.add_input(dir)
        output = clone.run()
        step = (i + dirs[dir][0], j + dirs[dir][1])
        if output == 2:
            print(num_steps + 1)
            exit()
        if output and step not in visited:
            q.appendleft((clone, step, num_steps + 1))

