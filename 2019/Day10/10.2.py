import sys
from fractions import Fraction
from collections import defaultdict
from math import atan2, degrees, pi, sqrt
from itertools import cycle

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
map = [list(x) for x in data.split('\n')]

asteroids = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            asteroids.append((j,i))

# Part 1  - Find Base
visible_by_asteroid = []
for (x1,y1) in asteroids:
    unique_slopes = set()
    for (x2,y2) in asteroids:
        if (x1,y1) == (x2,y2):
            continue
        x_dist = x2 - x1
        y_dist = y2 - y1
        if x_dist == 0:
            unique_slopes.add((0,1 if y_dist > 0 else -1))
        elif y_dist == 0:
            unique_slopes.add((1 if x_dist > 0 else -1,0))
        else:
            quad = 0
            if x_dist > 0 and y_dist > 0:
                quad = 1
            elif x_dist < 0 and y_dist > 0:
                quad = 2
            elif x_dist < 0 and y_dist < 0:
                quad = 3
            else:
                quad = 4
            frac = Fraction(y_dist, x_dist)
            unique_slopes.add((quad,frac.numerator, frac.denominator))
    visible_by_asteroid.append((len(unique_slopes),(x1,y1)))

max_visible, new_base = max(visible_by_asteroid)

# Part 2 - Get slope and asteroid data for new base using angles
asteroids_by_angle = defaultdict(list)
(x1,y1) = new_base
for (x2,y2) in asteroids:
    if (x1,y1) == (x2,y2):
        continue
    x_dist = x2 - x1
    y_dist = y2 - y1
    dy,dx = y_dist,x_dist
    angle = (degrees(atan2(dy,dx)) + 90) % 360 
    asteroids_by_angle[angle].append((x2,y2))


# Sort so closest asteroid is first
for angle in asteroids_by_angle:
    asteroids_by_angle[angle].sort(key = lambda coord: sqrt(pow((coord[0] - new_base[0]),2) + pow((coord[1] - new_base[1]),2)), reverse=True)

# Sort angles
angle_order = cycle(sorted(asteroids_by_angle.keys()))
count = 0
last_removed = None
while count < 200:
    angle = next(angle_order)
    if asteroids_by_angle[angle]:
        last_removed = asteroids_by_angle[angle].pop()
        count += 1
print(last_removed[0] * 100 + last_removed[1])
