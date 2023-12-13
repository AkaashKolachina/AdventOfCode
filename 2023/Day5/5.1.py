import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]


def convert_num(num, map):
    for dst,src,step in map:
        if num >= src and num < src + step:
            return (num - src) + dst
    return num

seeds = []
maps = []
for line in lines:
    if line.strip().startswith("seeds"):
        match = re.compile(r'seeds:\s*([\d\s]+)').search(line)
        seeds = [int(x) for x in match.group(1).split()]
    elif "map" in line:
        maps.append([])
    elif line != '':
         matches = re.findall('\d+', line)
         maps[-1].append(tuple([int(x) for x in matches]))

min_location = float('inf')
for seed in seeds:
    val = seed
    for map in maps:
        val = convert_num(val,map)
    min_location = min(min_location, val)
print(min_location)