from sys import argv
from os import system
from time import sleep

def render_map():
    for i in range(len(map)):
        print(''.join(map[i]))

def draw_line(points):
    point_1 = points[0]
    point_2 = points[1]
    if point_1[0] == point_2[0]:
        start = min(point_1[1],point_2[1])
        end = max(point_1[1],point_2[1])
        for j in range(start, end + 1):
            map[j][point_1[0] - min_x] = rock
    else:
        start = min(point_1[0],point_2[0]) - min_x
        end = max(point_1[0],point_2[0]) - min_x
        for i in range(start, end + 1):
            map[point_1[1]][i] = rock

def draw_lines():
    for line in line_data:
        draw_line(line)

# Processing
input = []
with open(argv[1], "r") as f:
    input = f.readlines()

min_x = float("inf")
max_x = 0
max_y = 0
line_data = []
for line in input:
    lines = line.split(' -> ')
    for i in range(len(lines) - 1):
        start = lines[i].strip().split(',')
        end = lines[i + 1].strip().split(',')
        start_tuple = (int(start[0]), int(start[1]))
        end_tuple = (int(end[0]), int(end[1]))
        line_data.append((start_tuple,end_tuple))
        max_x = max(max_x, start_tuple[0], end_tuple[0])
        min_x = min(min_x, start_tuple[0], end_tuple[0])
        max_y = max(max_y, start_tuple[1], end_tuple[1])

do_vis = False
if len(argv) >= 3 and argv[2] == '-v':
    do_vis = True

# Simulation
air = '.'
rock = '#'
sand = 'o'
obstacles = set([rock,sand])
src = '+'
src_r = 0
src_c = 500 - min_x
map = [[air for i in range(max_x - min_x + 1)] for j in range(max_y + 1)]
map[src_r][src_c] = src
draw_lines()

num_sand = 0
is_running = True
moves = [[1,0], [1,-1], [1,1]]
while is_running:
    has_stopped = False
    sand_pos = [src_r + 1,src_c]
    while not has_stopped: 
        map[sand_pos[0]][sand_pos[1]] = sand
        if do_vis:
            system('clear')
            render_map()
        has_moved = False
        for move in moves:
            poss_move = [sand_pos[0] + move[0], sand_pos[1] + move[1]]
            if poss_move[0] > max_y or poss_move[1] > (max_x - min_x) or poss_move[1] < 0:
                is_running = False
                has_stopped = True
                has_moved = True
                break
            elif map[poss_move[0]][poss_move[1]] in obstacles:
                continue
            else:
                map[sand_pos[0]][sand_pos[1]] = air
                sand_pos = poss_move
                has_moved = True
                break
        if not has_moved:
            has_stopped = True
            num_sand +=1
print(num_sand)