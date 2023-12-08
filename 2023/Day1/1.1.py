import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

total = 0
for line in lines:
    first = int(re.search(r'\d', line).group())
    last = int(re.search(r'\d', line[::-1]).group())
    total += (first * 10 + last)

print(total)