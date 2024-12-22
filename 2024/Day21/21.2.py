import sys
from collections import deque, defaultdict, Counter
from itertools import product
from tqdm import tqdm
from functools import lru_cache

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

num_pad = [[7,8,9],[4,5,6],[1,2,3],[None,0,'A']]
direction_pad = [[None, '^','A'], ['<','v','>']]
dirs = {'^': (-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}
num_map = {7:(0,0), 8:(0,1), 9:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 1:(2,0), 2:(2,1), 3:(2,2), 0:(3,1), 'A':(3,2)}
direction_map = {'^': (0,1), 'A' : (0,2), '<' : (1,0), 'v' : (1,1), '>' : (1,2)}
cache = defaultdict(list)
grids = {"num_pad" : num_pad, "direction_pad": direction_pad}

def get_path(start_coords, end_coords, grid_name):
    grid = grids[grid_name]
    si,sj = start_coords
    ei,ej = end_coords
    di = ei - si
    dj = ej - sj
    horiz_path = ''
    vert_path = ''
    if di > 0:
        vert_path += 'v' * di
    else:
        vert_path += '^' * -di
    if dj > 0:
        horiz_path += '>' * dj
    else:
        horiz_path += '<' * -dj
    if grid[ei][sj] is not None and dj > 0:
        return vert_path + horiz_path + 'A'
    elif grid[si][ej] is not None:
        return horiz_path + vert_path + 'A'
    elif grid[ei][sj] is not None:
        #if vert_path + horiz_path + 'A' not in paths:
        return vert_path + horiz_path + 'A'

complexity = 0
for code in lines:
    start = 'A'
    num_path = []
    for num in code:
        if num.isnumeric():
            num = int(num)
        num_path.append(get_path(num_map[start], num_map[num],"num_pad"))
        start = num
    
    comp = Counter(num_path)
    for _ in range(25):
        new_count = Counter()
        for part in comp:
            path = []
            start = 'A'
            for p in part:
                path.append(get_path(direction_map[start], direction_map[p], "direction_pad"))
                start = p
            new_counter = Counter(path)
            for new_part in new_counter:
                new_counter[new_part] *= comp[part]
            for nc in new_counter:
                new_count[nc] += new_counter[nc]
        comp = new_count
    
    total_len = 0
    for part in comp:
        if comp[part] > 0:
            total_len += len(part) * comp[part]
    complexity += total_len * int(code[:-1])
print(complexity)