from sys import argv
import re
    
def move(steps):
    global dir
    for _ in range(steps):
        global cur
        next = ((cur[0] + dirs[dir][0]), (cur[1] + dirs[dir][1]))
        if grid[next[0]][next[1]] == ' ':
            while True:
                next = ((next[0] - dirs[dir][0]), (next[1] - dirs[dir][1]))
                if grid[next[0]][next[1]] == ' ':
                    break
            next = ((next[0] + dirs[dir][0]), (next[1] + dirs[dir][1]))
        if grid[next[0]][next[1]] == '#':
            break
        cur = next
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
print("row : {}".format(row))
print("col : {}".format(col))
print("facing : {}".format(dir))
print("password: {}".format(1000 * row + 4 * col + dir))