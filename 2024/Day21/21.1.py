import sys
from collections import deque
from itertools import product
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

num_pad = [[7,8,9],[4,5,6],[1,2,3],[None,0,'A']]
direction_pad = [[None, '^','A'], ['<','V','>']]
dirs = {'^': (-1,0), '>':(0,1), 'V':(1,0), '<':(0,-1)}
num_map = {7:(0,0), 8:(0,1), 9:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 1:(2,0), 2:(2,1), 3:(2,2), 0:(3,1), 'A':(3,2)}
direction_map = {'^': (0,1), 'A' : (0,2), '<' : (1,0), 'V' : (1,1), '>' : (1,2)}

def bfs(start_coords, end_coords, grid):
    paths = []
    q = deque([(start_coords,0,'',frozenset())])
    shortest_len = None
    while len(q):
        (i,j),dist,path,visited = q.pop()
        if (i,j) == end_coords:
            if not shortest_len:
                shortest_len = dist
            elif dist > shortest_len:
                break
            path += 'A'

            paths.append(path)
        elif (i,j) in visited:
            continue
        else:
            visited = frozenset(visited | {(i,j)})
            for dir in dirs:
                di,dj = dirs[dir]
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i+di][j+dj] is not None:
                    q.appendleft(((i+di,j+dj), dist + 1, path + dir, visited))
    return paths

complexity = 0
for code in lines:
    start = 'A'
    shortest_num_codes = []
    for num in code:
        if num.isnumeric():
            num = int(num)
        paths = bfs(num_map[start], num_map[num],num_pad)
        shortest_num_codes.append(paths)
        start = num
    shortest_paths = [''.join(item) for item in product(*shortest_num_codes)]
    
    shortest_dir_1_paths = []
    for path in shortest_paths:
        dir1_start = 'A'
        dir1_sub_paths = []
        for dir1 in path:
            dir1_paths = bfs(direction_map[dir1_start], direction_map[dir1], direction_pad)
            dir1_sub_paths.append(dir1_paths)
            dir1_start = dir1
        shortest_dir_1_paths += [''.join(item) for item in product(*dir1_sub_paths)]
    
    min_len = min(len(s) for s in shortest_dir_1_paths)
    shortest_dir_1_paths = [s for s in shortest_dir_1_paths if len(s) == min_len]
    shortest_dir_2_paths = []
    for path in shortest_dir_1_paths:
        dir2_start = 'A'
        dir2_sub_paths = []
        for dir2 in path:
            dir2_paths = bfs(direction_map[dir2_start], direction_map[dir2], direction_pad)
            dir2_sub_paths.append(dir2_paths)
            dir2_start = dir2
        shortest_dir_2_paths += [''.join(item) for item in product(*dir2_sub_paths)]
    
    min_len = min(len(s) for s in shortest_dir_2_paths)
    shortest_dir_2_paths = [s for s in shortest_dir_2_paths if len(s) == min_len]
    complexity += len(shortest_dir_2_paths[0]) * int(code[:-1])
print(complexity)