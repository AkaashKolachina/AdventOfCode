import sys
from fractions import Fraction

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
map = [list(x) for x in data.split('\n')]

asteroids = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            asteroids.append((j,i))

max_visible = 0
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
    max_visible = max(max_visible, len(unique_slopes))

print(max_visible)