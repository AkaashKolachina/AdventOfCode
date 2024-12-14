import sys
import re
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

positions = []
velocities = []

for line in lines:
    pos,vel = line.split()
    px,py= map(int,re.findall(r"-?\d+",pos))
    vx,vy= map(int,re.findall(r"-?\d+",vel))
    positions.append((px,py))
    velocities.append((vx,vy))

NUM_ROWS = 103
NUM_COLS = 101
for steps in tqdm(range(10000)):
    grid = [['.'for x in range(NUM_COLS)] for y in range(NUM_ROWS)]
    for i in range(len(positions)):
        px,py = positions[i]
        vx,vy = velocities[i]
        px += vx
        py += vy
        px %= NUM_COLS
        py %= NUM_ROWS
        positions[i] = (px,py)

        for px,py in positions:
            grid[py][px] = '#'
    if any('#########' in ''.join(row) for row in grid):
        print("Steps: " + str(steps))
        for row in grid:
            print(''.join(row))
        print('\n')

