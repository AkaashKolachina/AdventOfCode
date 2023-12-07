from sys import argv
import ast
from functools import cmp_to_key

def compare_nums(left,right):
    if left < right:
        return -1
    elif right < left:
        return 1
    else:
        return 0


def compare_packets(left,right):
    for i in range(max(len(left),len(right))):
        if i >= len(left):
            return -1
        if i >= len(right):
            return 1
        to_ret = 0
        l = left[i]
        r = right[i]
        if isinstance(l,int):
            if isinstance(r,int):
                to_ret = compare_nums(l,r)
            else:
                to_ret = compare_packets([l], r)
        elif isinstance(r,int):
            to_ret = compare_packets(l, [r])
        else:
            to_ret = compare_packets(l,r)
        
        if to_ret == 1 or to_ret == -1:
            return to_ret

lines = []
with open(argv[1], "r") as f:
    lines = f.readlines()

packets = [[2],[6]]
for i in range(0,len(lines),3):
    left = ast.literal_eval(lines[i].strip())
    right = ast.literal_eval(lines[i + 1].strip())
    packets.append(left)
    packets.append(right)


sorted = sorted(packets,key=cmp_to_key(compare_packets))
indices = []
for i in range(len(sorted)):
    if sorted[i] == [2] or sorted[i] == [6]:
        indices.append(i + 1)
print(indices[0] * indices[1])
