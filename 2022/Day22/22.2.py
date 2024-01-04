from sys import argv
import re
from collections import defaultdict

def wrap():
    if faces[cur] == 1:
        if dir_chars[dir] == 'L':
            diff = face_bounds[1][2][0] - cur[0]
            new_r = face_bounds[4][0][0] + diff
            new_c = face_bounds[4][0][1]
            return (new_r,new_c), 0
        elif dir_chars[dir] == 'U':
            diff = (cur[1] - face_bounds[1][0][1])
            new_r = face_bounds[6][0][0] + diff
            new_c = face_bounds[6][0][1]
            return (new_r,new_c), 0
    elif faces[cur] == 2:
        if dir_chars[dir] == 'R':
            diff = face_bounds[2][3][0] - cur[0]
            new_r = face_bounds[5][1][0] +  diff
            new_c = face_bounds[5][1][1]
            return (new_r,new_c), 2
        elif dir_chars[dir] == 'U':
            diff = face_bounds[2][1][1] - cur[1]
            new_c = face_bounds[6][3][1] - diff
            new_r = face_bounds[6][3][0]
            return (new_r,new_c), 3
        elif dir_chars[dir] == 'D':
            diff = cur[1] - face_bounds[2][2][1]
            new_r = face_bounds[3][1][0] + diff
            new_c = face_bounds[3][1][1]
            return (new_r,new_c), 2
    elif faces[cur] == 3:
        if dir_chars[dir] == 'L':
            diff = face_bounds[3][2][0] - cur[0]
            new_c = face_bounds[4][1][1] - diff
            new_r = face_bounds[4][1][0]
            return (new_r,new_c), 1
        elif dir_chars[dir] == 'R':
            diff = cur[0] - face_bounds[3][1][0]
            new_c = face_bounds[2][2][1] + diff
            new_r = face_bounds[2][2][0]
            return (new_r,new_c),3
    elif faces[cur] == 4:
        if dir_chars[dir] == 'U':
            diff = face_bounds[4][1][1] - cur[1]
            new_r = face_bounds[3][2][0] - diff
            new_c = face_bounds[3][2][1]
            return (new_r,new_c), 0
        elif dir_chars[dir] == 'L':
            diff = cur[0] - face_bounds[4][0][0] 
            new_r = face_bounds[1][2][0] - diff
            new_c = face_bounds[1][2][1]
            return (new_r,new_c), 0
    elif faces[cur] == 5:
        if dir_chars[dir] == 'R':
            diff =  cur[0] - face_bounds[5][1][0]
            new_r = face_bounds[2][3][0] - diff
            new_c = face_bounds[2][3][1]
            return (new_r,new_c), 2
        elif dir_chars[dir] == 'D':
            diff = cur[1] - face_bounds[5][2][1]
            new_r = face_bounds[6][1][0] + diff
            new_c = face_bounds[6][1][1]
            return (new_r,new_c), 2
    elif faces[cur] == 6:
        if dir_chars[dir] == 'R':
            diff = cur[0] - face_bounds[6][1][0]
            new_c = face_bounds[5][2][1] + diff
            new_r = face_bounds[5][2][0]
            return (new_r,new_c),3
        elif dir_chars[dir] == 'L':
            diff = cur[0] - face_bounds[6][0][0]
            new_c = face_bounds[1][0][1] + diff
            new_r = face_bounds[1][0][0]
            return (new_r,new_c),1
        elif dir_chars[dir] == 'D':
            diff = face_bounds[6][3][1] - cur[1]
            new_c = face_bounds[2][1][1] - diff
            new_r = face_bounds[2][1][0]
            return (new_r,new_c), 1

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
face_len = 0
for c in grid[1]:
    if c != ' ':
        face_len += 1
face_len = int(face_len / 2)

for r in range(1,face_len + 1):
    face = 1
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 1 or r == face_len):
            face_bounds[face].append((r,c))
        elif count == face_len and (r == 1 or r == face_len):
            face_bounds[face].append((r,c))
            if face == 2:
                break
            count = 0
            face += 1
        elif count == face_len:
            if face == 2:
                break
            count = 0
            face += 1

for r in range(face_len + 1,2 * face_len + 1):
    face = 3
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == face_len + 1 or r == 2 * face_len):
            face_bounds[face].append((r,c))
        elif count == face_len and (r == face_len + 1 or r == 2 * face_len):
            face_bounds[face].append((r,c))
            break

for r in range(2 * face_len + 1,3 * face_len + 1):
    face = 4
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 2 * face_len + 1 or r == 3 * face_len):
            face_bounds[face].append((r,c))
        elif count == face_len and  (r == 2 * face_len + 1 or r == 3 * face_len):
            face_bounds[face].append((r,c))
            if face == 5:
                break
            count = 0
            face += 1
        elif count == face_len:
            if face == 5:
                break
            count = 0
            face += 1

for r in range(3 * face_len + 1,4 * face_len + 1):
    face = 6
    count = 0
    for c in range(len(grid[0])):
        if grid[r][c] == ' ':
            continue
        faces[(r,c)] = face
        count += 1
        if count == 1 and (r == 3 * face_len + 1 or r == 4 * face_len):
            face_bounds[face].append((r,c))
        elif count == face_len and  (r == 3 * face_len + 1 or r == 4 * face_len):
            face_bounds[face].append((r,c))
            break
'''
for r in range(len(grid)):
    for c in range(len(grid[0])):
        grid[r][c] = str(faces[(r,c)])
for bounds in face_bounds.values():
    for point in bounds:
        grid[point[0]][point [1]] = 'b'
grid[64][150] = 'X'
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
#for r in range(len(grid)):
#        print(''.join(grid[r]))
print("row : {}".format(row))
print("col : {}".format(col))
print("facing : {}".format(dir))
print("password: {}".format(1000 * row + 4 * col + dir))