import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

robots = []

for line in lines:
    pos,vel = line.split()
    px,py= map(int,re.findall(r"-?\d+",pos))
    vx,vy= map(int,re.findall(r"-?\d+",vel))
    robots.append([(px,py),(vx,vy)])

NUM_ROWS = 103
NUM_COLS = 101
quad_1 = 0
quad_2 = 0
quad_3 = 0
quad_4 = 0
for robot in robots:
    p,v = robot
    px,py = p
    vx,vy = v
    for _ in range(100):
        px += vx
        py += vy
        px %= NUM_COLS
        py %= NUM_ROWS
    if px < (NUM_COLS // 2) and py < (NUM_ROWS // 2):
        quad_1 += 1
    elif px > (NUM_COLS // 2)  and py < (NUM_ROWS // 2):
        quad_2 += 1
    elif px < (NUM_COLS // 2) and py > (NUM_ROWS // 2):
        quad_3 += 1
    elif px > (NUM_COLS // 2)  and py > (NUM_ROWS // 2):
        quad_4 += 1

print(quad_1 * quad_2 * quad_3 * quad_4)