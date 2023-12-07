from sys import argv
from collections import deque

def explore_neighbors(pos, nodes_in_next_level,visited):
    dir_r = [-1,1,0,0]
    dir_c = [0,0,1,-1]
    for i in range(len(dir_r)):
        neighbor = [pos[0] + dir_r[i], pos[1] + dir_c[i]]

        if neighbor[0] < 0 or neighbor[1] < 0:
            continue
        elif neighbor[0] >= num_rows or neighbor[1] >= num_cols:
            continue
        elif visited[neighbor[0]][neighbor[1]]:
            continue
        elif grid[neighbor[0]][neighbor[1]] > (grid[pos[0]][pos[1]] + 1):
            continue
        q.append(neighbor)
        visited[neighbor[0]][neighbor[1]] = True
        nodes_in_next_level += 1
    return nodes_in_next_level



def bfs(start):
    visited = [[False for i in range(num_cols)] for j in range(num_rows)]
    nodes_left_in_level = 1
    nodes_in_next_level = 0
    num_moves = 0
    is_end = False
    q.append([start[0], start[1]])
    visited[start[0]][start[1]] = True
    while len(q) > 0:
        point = q.popleft()
        if point[0] == end[0] and point[1] == end[1]:
            is_end = True
            break
        nodes_in_next_level = explore_neighbors(point,nodes_in_next_level,visited)
        nodes_left_in_level -= 1
        if nodes_left_in_level == 0:
            num_moves += 1
            nodes_left_in_level = nodes_in_next_level
            nodes_in_next_level = 0
    if is_end:
        return num_moves
    else:
        return float("inf")


### Processing
heights = {}
height = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    heights[letter] = height
    height += 1

grid = []
with open(argv[1], "r") as f:
    grid = f.readlines()

for i in range(len(grid)):
    grid[i] = list(grid[i].strip())

starts = []
end = ()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            starts.append((i,j))
            grid[i][j] = 0
        elif grid[i][j] == "E":
            end = (i,j)
            grid[i][j] = 25
        else:
            grid[i][j] = heights[grid[i][j]]
            if grid[i][j] == 0:
                starts.append((i,j))


### BFS
num_rows = len(grid)
num_cols = len(grid[0])

paths = []
for start in starts:
    q = deque()
    steps = bfs(start)
    paths.append(steps)

print(min(paths))