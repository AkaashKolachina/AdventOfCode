from sys import argv
from collections import deque

rocks = set()
left = set()
right = set()
up = set()
down = set()

## BFS
get_neighbors = lambda x,y,t : [((x, y), t + 1),((x - 1, y), t + 1),((x + 1, y), t + 1), ((x, y - 1), t + 1), ((x, y + 1), t + 1)]

def is_blocked(pos):
    return pos in rocks or pos in left or pos in right or pos in up or pos in down

def update():
    global left,right,up,down
    left = list(left)
    for i in range(len(left)):
        left[i] = (left[i][0], left[i][1] - 1)
        if left[i] in rocks:
            left[i] = (left[i][0], len(map[0]) - 2)
    left = set(left)

    right = list(right)
    for i in range(len(right)):
        right[i] = (right[i][0], right[i][1] + 1)
        if right[i] in rocks:
            right[i] = (right[i][0], 1)
    right = set(right)

    up = list(up)
    for i in range(len(up)):
        up[i] = (up[i][0] - 1, up[i][1])
        if up[i] in rocks:
            up[i] = (len(map) - 2, up[i][1])
    up = set(up)

    down = list(down)
    for i in range(len(down)):
        down[i] = (down[i][0] + 1, down[i][1])
        if down[i] in rocks:
            down[i] = (1, down[i][1])
    down = set(down)

def explore_neighbors(pos, nodes_in_next_level,visited,q):
    neighbors = get_neighbors(pos[0][0],pos[0][1], pos[1])
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        elif is_blocked(neighbor[0]):
            continue
        q.append(neighbor)
        visited.add(neighbor)
        nodes_in_next_level += 1
    return nodes_in_next_level

def bfs(start, end):
    visited = set()
    q = deque()
    nodes_left_in_level = 1
    nodes_in_next_level = 0
    num_moves = 0
    is_end = False
    q.append((start,0))
    visited.add((start,0))
    while len(q) > 0:
        point = q.popleft()
        if point[0] == end:
            is_end = True
            break
        nodes_in_next_level = explore_neighbors(point,nodes_in_next_level,visited,q)
        nodes_left_in_level -= 1
        if nodes_left_in_level == 0:
            num_moves += 1
            nodes_left_in_level = nodes_in_next_level
            nodes_in_next_level = 0
            update()
    if is_end:
        return num_moves
    else:
        return float("inf")




## Processing 
data = open(argv[1]).read().strip()
map = [list(line) for line in data.split('\n')]

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '#':
            rocks.add((i,j))
        elif map[i][j] == '>':
            right.add((i,j))
        elif map[i][j] == '<':
            left.add((i,j))
        elif map[i][j] == '^':
            up.add((i,j))
        elif map[i][j] == 'v':
            down.add((i,j))

rocks |= set([(-1,i) for i in range(len(map[0]))])
rocks |= set([(len(map), i) for i in range(len(map[0]))])
start = (0, map[0].index('.'))
end = (len(map) - 1, map[-1].index('.'))

update()
first_trip = bfs(start,end)
second_trip = bfs(end,start) 
third_trip = bfs(start,end)
print(first_trip)
print(first_trip + second_trip + third_trip)
