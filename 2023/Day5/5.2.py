import sys
import re
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]


def convert_num(num, map):
    for src,dst,step in map:
        if num >= src and num < src + step:
            return (num - src) + dst
    return num




seeds = []
ranges = []
maps = []
for line in lines:
    if line.strip().startswith("seeds"):
        match = re.compile(r'seeds:\s*([\d\s]+)').search(line)
        seed_data = [int(x) for x in match.group(1).split()]
        seed_starts = [seed_data[i] for i in range(len(seed_data)) if i % 2 == 0]
        ranges = [seed_data[i] for i in range(len(seed_data)) if i % 2 != 0]
        seeds = list(zip(seed_starts, ranges))
    elif "map" in line:
        maps.append([])
    elif line != '':
         matches = re.findall('\d+', line)
         maps[-1].append(tuple([int(x) for x in matches]))


rev_maps = maps[::-1]
min_location = 0
found_min_loc = False
while not found_min_loc:
    val = min_location
    for map in rev_maps:
        val = convert_num(val, map)
    for seed_start, seed_range in seeds:
        if seed_start <= val < seed_start + seed_range:
            print(min_location)
            found_min_loc = True
            break
    min_location += 1