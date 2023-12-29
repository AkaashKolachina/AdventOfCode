import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]
start = (0,grid[0].index('.'))
end = (len(grid) - 1, grid[-1].index('.'))

LEFT = (0,-1)
RIGHT = (0,1)
UP = (-1,0)
DOWN = (1,0)
dirs = [LEFT, RIGHT, UP, DOWN]
slopes = {">": RIGHT, "<": LEFT, "^":UP, "v":DOWN}

def get_neighbors(i,j):
    neighbors = []
    if grid[i][j] in slopes:
        di,dj = slopes[grid[i][j]]
        neighbors.append((i + di, j + dj))
    else:
        for di,dj in dirs:
            neighbors.append((i + di, j + dj))  

    neighbors = [(i,j) for (i,j) in neighbors if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != '#']
    return neighbors   

max_steps = 0
stack = [(start[0], start[1], 0, set())]
while stack:
    i,j,num_steps,visited = stack.pop()
    if (i,j) == end:
        max_steps = max(max_steps, num_steps)
    else:
        neighbors = get_neighbors(i,j)
        for nb in neighbors:
            if nb not in visited:
                stack.append((nb[0], nb[1], num_steps + 1, visited | {nb}))
print(max_steps)