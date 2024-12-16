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

def move_boxes(boxes_lst,di,dj):
    for (i1,j1), (i2,j2) in boxes_lst:
        if (i1+di,j1+dj) in walls or (i2+di,j2+dj) in walls:
            return
    next_pos = []
    for box in boxes_lst:
        next_pos.append(((box[0][0] + di, box[0][1] + dj), (box[1][0] + di, box[1][1] + dj)))
    points = {p for b in next_pos for p in b}
    next_boxes = [box for box in boxes if box[0] in points or box[1] in points]
    if len(next_boxes) == 0:
        for box in boxes_lst:
            boxes.remove(box)
            boxes.add(((box[0][0] + di, box[0][1] + dj), (box[1][0] + di, box[1][1] + dj)))
    elif len(next_boxes) == 1:
        move_box(next_boxes[0],di,dj)
        next_boxes = [box for box in boxes if box[0] in points or box[1] in points]
        if len(next_boxes) == 0:
            for box in boxes_lst:
                boxes.remove(box)
                boxes.add(((box[0][0] + di, box[0][1] + dj), (box[1][0] + di, box[1][1] + dj)))
    else:
        move_boxes(next_boxes,di,dj)
        next_boxes = [box for box in boxes if box[0] in points or box[1] in points]
        if len(next_boxes) == 0:
            for box in boxes_lst:
                boxes.remove(box)
                boxes.add(((box[0][0] + di, box[0][1] + dj), (box[1][0] + di, box[1][1] + dj)))

def move_box(box,di,dj):
    (i1,j1), (i2,j2) = box
    next_pos = (((i1+di,j1+dj), (i2+di,j2+dj)))
    if (i1+di,j1+dj) in walls or (i2+di,j2+dj) in walls:
        return
    if di != 0:
        next_boxes = [box for box in boxes if box[0] in next_pos or box[1] in next_pos]
        if next_boxes == []:
            boxes.remove(box)
            boxes.add(next_pos)
        elif len(next_boxes) == 1:
            move_box(next_boxes[0],di,dj)
            next_boxes = [box for box in boxes if box[0] in next_pos or box[1] in next_pos]
            if next_boxes == []:
                boxes.remove(box)
                boxes.add(next_pos)
        else:
            move_boxes(next_boxes,di,dj)
            next_boxes = [box for box in boxes if box[0] in next_pos or box[1] in next_pos]
            if next_boxes == []:
                boxes.remove(box)
                boxes.add(next_pos)
    else:
        next_box = ((box[0][0] + 2*di, box[0][1] + 2*dj), (box[1][0] + 2*di, box[1][1] + 2*dj))
        if next_box not in boxes:
            boxes.remove(box)
            boxes.add(next_pos)
        else:
            move_box(next_box,di,dj)
            if next_box not in boxes:
                boxes.remove(box)
                boxes.add(next_pos)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            start = (i,j * 2)
        elif grid[i][j] == 'O':
            boxes.add((((i,j*2),(i, (j*2) + 1))))
        elif grid[i][j] == '#':
            walls.add((i,j*2))
            walls.add((i, (j*2) + 1))
        
cur = start

for dir in moves:
    big_grid = [['.' for x in range(2*len(grid[0]))] for y in range(len(grid))]  
    di,dj = dirs[dir]
    i,j = cur
    i2 = i + di
    j2 = j + dj
    if (i2,j2) in walls:
        continue
    else:
       next_box = next((box for box in boxes if (i2,j2) in box), None)
       if next_box:
        move_box(next_box,di,dj)
       next_box = next((box for box in boxes if (i2,j2) in box), None)
       if not next_box:
           cur = (i2,j2)


gps_sum = 0
for box in boxes:
    gps_sum += (box[0][0] * 100 + box[0][1])
print(gps_sum)