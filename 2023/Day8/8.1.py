import sys
from itertools import cycle
from collections import defaultdict
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
instr, *map_lines = data.split('\n')
map_lines = [line for line in map_lines if line != '']

mp = defaultdict(dict)
for line in map_lines:
    coords = re.match(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)',line)
    mp[coords.group(1)]['R'] = coords.group(3)
    mp[coords.group(1)]['L'] = coords.group(2)

start = 'AAA'
end = 'ZZZ'
cur_loc = start
num_steps = 0
for dir in cycle(instr):
    if cur_loc == end:
        print(num_steps)
        break
    else:
        num_steps += 1
        cur_loc = mp[cur_loc][dir]