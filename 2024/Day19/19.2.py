import sys
from functools import lru_cache

input = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

towels = lines[0].split(', ')
patterns = lines[2:]

@lru_cache(None)
def has_match(i, pattern):
    if i == len(pattern):
        return 1
    elif i > len(pattern):
        return 0 

    count = 0
    for towel in towels:
        if pattern.startswith(towel, i):
            count += has_match(i + len(towel), pattern)
    return count

count = 0
for pattern in patterns:
    count += has_match(0, pattern)

print(count)
