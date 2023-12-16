import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

time = int(''.join(re.findall(r'\d+',lines[0])))
dist = int(''.join(re.findall(r'\d+',lines[1])))

def get_dist(i):
    return i*(time - i)

def comp_min():
    left = 0
    right = time
    while left < right:
        mid = (left + right) // 2
        # mid should always be > 0 and < time
        if get_dist(mid - 1) < dist and get_dist(mid + 1) > dist:
            return mid
        elif get_dist(mid - 1) < dist and get_dist(mid + 1) < dist:
            left = mid + 1
        else:
            right = mid - 1

def comp_max():
    left = 0
    right = time
    while left < right:
        mid = (left + right) // 2
        if get_dist(mid - 1) > dist and get_dist(mid + 1) < dist:
            return mid
        elif get_dist(mid - 1) < dist and get_dist(mid + 1) < dist:
            right = mid - 1
        else:
            left = mid + 1

print(comp_max() - comp_min())
