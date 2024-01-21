import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

moons = []
for line in lines:
    pos = []
    match = re.search(r'x=(-?\d+), y=(-?\d+), z=(-?\d+)', line)
    for i in range(1,4):
        pos.append(int(match.group(i)))
    moons.append((pos,[0,0,0]))

for _ in range(1000):
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

total_energy = 0
for moon in moons:
    total_energy +=  (sum([abs(x) for x in moon[0]]) * sum([abs(x) for x in moon[1]]))


print(total_energy)