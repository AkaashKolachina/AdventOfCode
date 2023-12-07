from sys import argv
import re
from collections import defaultdict

def wrap():
    if faces[cur] == 1:
        if dir_chars[dir] == 'L':
            if cur[0] < (face_bounds[1][0][0] + 25):
                new_r = (face_bounds[4][2][0] - (cur[0] - face_bounds[1][0][0]))
                new_c = face_bounds[4][2][1]
                return (new_r,new_c), 0
            else:
                new_r = (face_bounds[4][0][0] + (face_bounds[1][2][0] - cur[0]))
                new_c = face_bounds[4][0][1]
                return (new_r,new_c), 0
        elif dir_chars[dir] == 'U':
            if cur[1] < (face_bounds[1][0][1] + 25):
                new_r = (face_bounds[6][0][0] + (cur[1] - face_bounds[1][2][1]))
                new_c = face_bounds[6][0][1]
                return (new_r,new_c), 0
            else:
                new_r = (face_bounds[6][2][0] - (face_bounds[1][1][1] - cur[1]))
                new_c = face_bounds[6][0][1]
                return (new_r,new_c), 0
    elif faces[cur] == 2:
        if dir_chars[dir] == 'R':
            if cur[0] < (face_bounds[2][1][0] + 25):
                new_r = (face_bounds[5][3][0] - (cur[0] - face_bounds[2][1][0]))
                new_c = face_bounds[5][1][1]
                return (new_r,new_c), 2
            else:
                new_r = (face_bounds[5][1][0] + (face_bounds[2][3][0] - cur[0]))
                new_c = face_bounds[5][1][1]
                return (new_r,new_c), 2
        elif dir_chars[dir] == 'U':
            if cur[1] < (face_bounds[2][0][1] + 25):
                new_r = face_bounds[6][2][0]
                new_c = (face_bounds[6][2][1] + (cur[1] - face_bounds[2][0][1]))
                return (new_r,new_c), 3
            else:
                new_r = face_bounds[6][2][0]
                new_c = (face_bounds[6][3][1] - (face_bounds[2][1][1] - cur[1]))
                return (new_r,new_c), 3
        elif dir_chars[dir] == 'D':
            pass


def move(steps):
    global dir
    for _ in range(steps):
        global cur
        is_wrapped = False
        next = ((cur[0] + dirs[dir][0]), (cur[1] + dirs[dir][1]))
        if grid[next[0]][next[1]] == ' ':
            next, new_dir = wrap()
            is_wrapped = True
        if grid[next[0]][next[1]] == '#':
            break
        cur = next
        if is_wrapped:
            dir = new_dir
        grid[cur[0]][cur[1]] = dir_chars[dir]


*grid, _, path = open(argv[1])
path = re.findall('(\d+|[A-Za-z]+)', path)

# grid processing
grid = [[' '] + list(line)[:-1] + [' '] for line in grid]
max_len = max(len(x) for x in grid)
for i in range(len(grid)):
    pad = [' '] * (max_len - len(grid[i]))
    grid[i] = grid[i] + pad
grid = [[' '] * max_len] + grid + [[' '] * max_len]

# map faces
faces = defaultdict(int)
face_bounds = defaultdict(list) # top left top right bottom left bottom right
for r in range(1,51):
    face = 1
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 1 or r == 50):
            face_bounds[face].append((r,c))
        elif count == 50 and (r == 1 or r == 50):
            face_bounds[face].append((r,c))
            if face == 2:
                break
            count = 0
            face += 1

for r in range(51,101):
    face = 3
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 51 or r == 100):
            face_bounds[face].append((r,c))
        elif count == 50 and (r == 51 or r == 100):
            face_bounds[face].append((r,c))
            break

for r in range(101,151):
    face = 4
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 101 or r == 150):
            face_bounds[face].append((r,c))
        elif count == 50 and (r == 101 or r == 150):
            face_bounds[face].append((r,c))
            if face == 5:
                break
            count = 0
            face += 1

for r in range(151,201):
    face = 6
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 151 or r == 200):
            face_bounds[face].append((r,c))
        elif count == 50 and  (r == 151 or r == 200):
            face_bounds[face].append((r,c))
            break
'''
for r in range(len(grid)):
    for c in range(len(grid[0])):
        grid[r][c] = str(faces[(r,c)])
for bounds in face_bounds.values():
    for point in bounds:
        grid[point[0]][point [1]] = 'b'
for r in range(len(grid)):
        print(''.join(grid[r]))
'''

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
dir_chars = ['R', 'D', 'L', 'U']
dir = 0
delta = {'R' : 1, 'L' : -1}

cur = (1,grid[1].index('.'))


for i in range(len(path)):
    if path[i].isnumeric():
        steps = int(path[i])
        move(steps)
    else:
        dir = (dir + delta[path[i]]) % len(dirs)


row = cur[0] 
col = cur[1] 
grid[cur[0]][cur[1]] = 'E'
for r in range(len(grid)):
        print(''.join(grid[r]))
print("row : {}".format(row))
print("col : {}".format(col))
print("facing : {}".format(dir))
print("password: {}".format(1000 * row + 4 * col + dir))