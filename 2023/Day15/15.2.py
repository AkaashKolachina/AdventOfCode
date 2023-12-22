import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
sequence = [x for x in data.split(',')]

boxes = [[] for _ in range(256)]
fl_map = {}

def HASH(seq):
    cur_val = 0
    for c in seq:
        cur_val += ord(c)
        cur_val *= 17
        cur_val %= 256
    return cur_val

for seq in sequence:
    parts = seq.split('=')
    if len(parts) == 1:
        label = seq[:-1]
        if fl_map.get(label,-1) != -1:
            boxes[HASH(label)].remove(label)
        fl_map[label] = -1
    else:
        label = parts[0]
        fl = int(parts[1])
        if fl_map.get(label,-1) == -1:
            boxes[HASH(label)].append(label)
        fl_map[label] = fl

total = 0
for i,box in enumerate(boxes):
    slot_num = 1
    for label in box:
        if fl_map[label] != -1:
            focus_power = ((i + 1) * fl_map[label] * slot_num)
            total += focus_power
            slot_num += 1
print(total)