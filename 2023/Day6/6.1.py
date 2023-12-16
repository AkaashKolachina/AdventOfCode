import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

times = re.findall(r'\d+',lines[0])
dists = re.findall(r'\d+',lines[1])
data = [(int(times[i]), int(dists[i])) for i in range(len(times))]

prod = 1
for t,d in data:
    num_ways = 0
    for i in range(t+1):
        if i * (t - i) > d:
            num_ways += 1
    prod *= num_ways
print(prod)