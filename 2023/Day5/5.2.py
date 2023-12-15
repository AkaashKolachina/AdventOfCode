import sys
import re
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]


def convert_num(num, map):
    for dst,src,step in map:
        if num >= src and num < src + step:
            return (num - src) + dst
    return num

def map_range(ranges, map):
    proceessed = []
    for dst,src,step in map:
        buffer = []
        for entry in ranges:
            start = entry[0]
            end = start + entry[1]
            src_end = src + step
            pre = (start,min(end,src))
            overlap = (max(start, src), min(src_end, end))
            post = (max(src_end, start), end)
            if pre[1] > pre[0]:
                buffer.append(pre)
            if overlap[1] > overlap[0]:
                proceessed.append((overlap[0]-src+dst, overlap[1]-src+dst))
            if post[1] > post[0]:
                buffer.append(post)
        ranges = buffer
    return ranges + proceessed


seeds = []
ranges = []
maps = []
for line in lines:
    if line.strip().startswith("seeds"):
        match = re.compile(r'seeds:\s*([\d\s]+)').search(line)
        seed_data = [int(x) for x in match.group(1).split()]
        seed_starts = [seed_data[i] for i in range(len(seed_data)) if i % 2 == 0]
        ranges = [seed_data[i] for i in range(len(seed_data)) if i % 2 != 0]
        seeds = zip(seed_starts, ranges)
    elif "map" in line:
        maps.append([])
    elif line != '':
         matches = re.findall('\d+', line)
         maps[-1].append(tuple([int(x) for x in matches]))

for seed in seeds:
    ranges = [seed]
    for map in maps:
        ranges = map_range(ranges, map)
    print(min(ranges))