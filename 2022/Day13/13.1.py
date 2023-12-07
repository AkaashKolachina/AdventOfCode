from sys import argv
import ast

def compare_nums(left,right):
    if left < right:
        return 1
    elif right < left:
        return -1
    else:
        return 0


def compare_packets(left,right):
    for i in range(max(len(left),len(right))):
        if i >= len(left):
            return 1
        if i >= len(right):
            return -1
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

index = 0
correct = []
for i in range(0,len(lines),3):
    index += 1
    left = ast.literal_eval(lines[i].strip())
    right = ast.literal_eval(lines[i + 1].strip())
    
    if compare_packets(left,right) == 1:
        correct.append(index)

print(sum(correct))
