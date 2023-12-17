import sys
from itertools import cycle
from collections import defaultdict
import re
import numpy as np

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
instr, *map_lines = data.split('\n')
map_lines = [line for line in map_lines if line != '']

mp = defaultdict(dict)
starts = []
ends = []
for line in map_lines:
    coords = re.match(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)',line)
    loc = coords.group(1)
    mp[loc]['R'] = coords.group(3)
    mp[loc]['L'] = coords.group(2)
    if loc[-1] == 'A':
        starts.append(loc)
    elif loc[-1] == 'Z':
        ends.append(loc)

ends = set(ends)
min_steps = []
for start in starts:
    cur_loc = start
    num_steps = 0
    for dir in cycle(instr):
        if cur_loc in ends:
            min_steps.append(num_steps)
            break
        else:
            num_steps += 1
            cur_loc = mp[cur_loc][dir]
print(np.lcm.reduce(min_steps))