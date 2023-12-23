import sys
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

def get_neighbors(entry):
    pos,dir = entry
    neighbors = []
    i,j = pos
    if dir == (0,1): # right
        if grid[i][j] == '|':
            neighbors.append(((i + 1, j), (1,0)))
            neighbors.append(((i - 1, j), (-1,0)))
        elif grid[i][j] == '\\':
            neighbors.append(((i + 1, j), (1,0)))
        elif grid[i][j] == '/':
            neighbors.append(((i - 1, j), (-1,0)))
        else:
            neighbors.append(((i + dir[0], j + dir[1]),dir))
    elif dir == (0,-1): # left
        if grid[i][j] == '|':
            neighbors.append(((i - 1, j), (-1,0)))
            neighbors.append(((i + 1, j), (1,0)))
        elif grid[i][j] == '\\':
            neighbors.append(((i - 1, j), (-1,0)))
        elif grid[i][j] == '/':
            neighbors.append(((i + 1, j), (1,0)))
        else:
            neighbors.append(((i + dir[0], j + dir[1]),dir))
    elif dir == (1,0): # down
        if grid[i][j] == '-':
            neighbors.append(((i, j + 1), (0,1)))
            neighbors.append(((i, j - 1), (0,-1)))
        elif grid[i][j] == '\\':
            neighbors.append(((i, j + 1), (0,1)))
        elif grid[i][j] == '/':
            neighbors.append(((i, j - 1), (0,-1)))
        else:
            neighbors.append(((i + dir[0], j + dir[1]),dir))
    elif dir == (-1,0): # up
        if grid[i][j] == '-':
            neighbors.append(((i, j - 1), (0,-1)))
            neighbors.append(((i, j + 1), (0,1)))
        elif grid[i][j] == '\\':
            neighbors.append(((i, j - 1), (0,-1)))
        elif grid[i][j] == '/':
            neighbors.append(((i, j + 1), (0,1)))
        else:
            neighbors.append(((i + dir[0], j + dir[1]),dir))
    return [((i,j),dir) for ((i,j),dir) in neighbors if 0 <= i < len(grid) and 0 <= j < len(grid[0])]


visited = set()
q = deque([((0,0), (0,1))])

while len(q):
    entry = q.pop()
    if entry in visited:
        continue
    visited.add(entry)
    neighbors = get_neighbors(entry)
    for nb in neighbors:
        q.appendleft(nb)

energized = {pos for (pos,_) in visited}
print(len(energized))
    
