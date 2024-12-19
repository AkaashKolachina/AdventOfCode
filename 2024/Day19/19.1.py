import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

towels = lines[0].split(', ')
patterns = lines[2:]

def has_match(pattern,i):
    if i == len(pattern):
        return True
    elif i > len(pattern):
        return False
    
    can_make = False
    for towel in towels:
        if pattern.startswith(towel, i):
            can_make = can_make or has_match(pattern, i + len(towel))
    return can_make

count = 0
for pattern in patterns:
    if has_match(pattern,0):
        count += 1
print(count)