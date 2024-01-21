import sys
import re
import numpy as np

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

moons = []
start_state = []
for line in lines:
    pos = []
    match = re.search(r'x=(-?\d+), y=(-?\d+), z=(-?\d+)', line)
    for i in range(1,4):
        pos.append(int(match.group(i)))
    moons.append((pos,[0,0,0]))
    start_state.append(pos.copy())

def found_cycle(idx):
    for i,moon in enumerate(moons):
        if moon[0][idx] != start_state[i][idx] or moon[1][idx] != 0:
            return False
    return True

cycles = {}
num_steps = 0
while len(cycles) < 3:
    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            moon_1 = moons[i]
            moon_2 = moons[j]
            for coord_idx in range(3):
                if moon_1[0][coord_idx] > moon_2[0][coord_idx]:
                    moon_1[1][coord_idx] -= 1
                    moon_2[1][coord_idx] += 1
                elif moon_1[0][coord_idx] < moon_2[0][coord_idx]:
                    moon_1[1][coord_idx] += 1
                    moon_2[1][coord_idx] -= 1

    for moon in moons:
        for i in range(3):
            moon[0][i] += moon[1][i]
    num_steps += 1

    for i in range(3):
        if i not in cycles and found_cycle(i):
            cycles[i] = num_steps

print(np.lcm.reduce(list(cycles.values())))