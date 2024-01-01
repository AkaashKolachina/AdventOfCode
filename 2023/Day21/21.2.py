import sys
from collections import deque
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

start = None
start_found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i,j)
            start_found = True
            break
    if start_found:
        break
grid[start[0]][start[1]] = '.' 
start = (start[0] + len(grid)*4, start[1] + len(grid[0]*4))   

# Expand grid to get first few data points
expanded_grid = []
for _ in range(9):
    for line in grid:
        expanded_grid.append(line * 9)
grid = expanded_grid

def get_neighbors(i,j):
    neighbors = []
    for di,dj in dirs:
        neighbors.append((i + di, j + dj))
    neighbors = [(i2,j2) for (i2,j2) in neighbors if grid[i2][j2] != '#'] 
    return neighbors

# From day 9
'''
def get_next(data):
    if all([x == 0 for x in data]):
        return 0
    
    diffs = ()
    if data[:-1] in memo:
        diffs = memo[data[:-1]] + ((data[-1]),)
    else:
        diffs = []
        for i in range(1,len(data)):
            diffs.append(data[i] - data[i - 1])
        diffs = tuple(diffs)

    memo[data] = diffs
    next_val = get_next(diffs)
    return next_val + data[-1]
'''
def get_next(data):
    if all([x == 0 for x in data]):
        return 0
    
    diffs = []
    for i in range(1,len(data)):
        diffs.append(data[i] - data[i - 1])
    
    next_val = get_next(diffs)
    return next_val + data[-1]

# 26501365 = 202300 * 131 + 65 (Thanks AOC subreddit)
# Brute force first few steps of the sequence as a baseline then use day 9 code to extrapolate the rest
'''
baseline_steps = [65 + i*131 for i in range(4)]
baselines = []
visited = set()
q = deque([(start,0)])
num_steps = 0
max_step_idx = 0
max_steps = baseline_steps[max_step_idx]
last_step = set()
while q:
    entry = q.pop()
    (i,j), num_steps = entry
    if entry in visited:
        continue
    visited.add(entry)
    for nb in get_neighbors(i,j):
        if num_steps == max_steps - 1:
            last_step.add(nb)
        q.appendleft((nb, num_steps + 1))
    if num_steps == max_steps:
        print(f'{max_steps}: {len(last_step)}')
        max_step_idx += 1
        if max_step_idx == len(baseline_steps):
            break
        max_steps = baseline_steps[max_step_idx]
        last_step = set()
'''
sequence = [3734,33285,92268,180683] # found from running the commented out code
memo = {}
for _ in tqdm(range(4, 202301)):
    next = get_next(sequence)
    sequence += (next,)

print(sequence[-1])