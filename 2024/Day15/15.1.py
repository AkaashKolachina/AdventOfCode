import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

grid = []
moves = ''
for i in range(len(lines)):
    if 'O' in lines[i] or '#' in lines[i] or '.' in lines[i]:
        grid.append(list(lines[i]))
    elif lines[i] == '':
        continue
    else:
        moves += lines[i]


dirs = {'>' : (0,1), 'v' : (1,0), '<' : (0,-1), '^': (-1,0)}
boxes = set()
walls = set()
start = (-1,-1)

def move_box(i,j,di,dj):
    if (i+di,j+dj) in walls:
        return
    if (i + di, j + dj) not in boxes:
        boxes.add((i + di, j + dj))
        boxes.remove((i, j))
    else:
        move_box(i+di,j+dj,di,dj)
        if (i + di, j + dj) not in boxes:
            boxes.add((i + di, j + dj))
            boxes.remove((i, j))


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            start = (i,j)
        elif grid[i][j] == 'O':
            boxes.add((i,j))
        elif grid[i][j] == '#':
            walls.add((i,j))
cur = start
for dir in moves:
    di,dj = dirs[dir]
    i,j = cur
    i2 = i + di
    j2 = j + dj
    if (i2,j2) in walls:
        continue
    else:
        if (i2,j2) in boxes:
            move_box(i2,j2,di,dj)
        if (i2,j2) not in boxes:
            cur = (i2,j2)

gps_sum = 0
for box in boxes:
    gps_sum += (box[0] * 100 + box[1])
print(gps_sum)