import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

time = int(''.join(re.findall(r'\d+',lines[0])))
dist = int(''.join(re.findall(r'\d+',lines[1])))

num_ways = 0

for i in range(time + 1):
    if i*(time - i) > dist:
        num_ways += 1
print(num_ways)

