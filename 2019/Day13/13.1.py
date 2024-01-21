import sys
sys.path.append('..')
from intcode import IntCode
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

tiles = defaultdict(int)
ic = IntCode(program.copy())
BLOCK = 2

has_halted = False
while not has_halted:
    tile_data = []
    for _ in range(3):
        tile_data.append(ic.run())
    if None in tile_data:
        has_halted = True
        break
    tiles[(tile_data[0], tile_data[1])] = tile_data[2]

print(list(tiles.values()).count(BLOCK))