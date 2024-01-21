import sys
from math import ceil
from collections import defaultdict
import heapq

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

reactions = {}
for line in lines:
    reaction,mineral = line.split('=>')
    quantity,mineral = mineral.strip().split()
    reactions[mineral] = ([], int(quantity))
    reaction = reaction.strip().split(',')
    for item in reaction:
        quant,item = item.split()
        reactions[mineral][0].append((item, int(quant)))
top_order = []
visited = set()
def top_sort(mineral):
    visited.add(mineral)
    if mineral in reactions:
        for item,_ in reactions[mineral][0]:
            if item not in visited:
                top_sort(item)
    top_order.append(mineral)

for key in reactions:
    if key not in visited:
        top_sort(key)
top_order = top_order[::-1]

def make_fuel(fuel_units):
    to_make = defaultdict(int)
    to_make['FUEL'] = fuel_units
    pq = [(0,'FUEL')]

    while pq:
        _,mineral = heapq.heappop(pq)
        if mineral == 'ORE':
            return to_make['ORE']
        reaction, quant_made = reactions[mineral]
        num_times = int(ceil(to_make[mineral] / quant_made))
        for m,q in reaction:
            to_make[m] += num_times * q
            entry = (top_order.index(m), m)
            if entry not in pq:
                heapq.heappush(pq,(top_order.index(m), m))

num_ores = 1000000000000
left = int(ceil(num_ores / make_fuel(1)))
right = 1000000000000
max_fuel = 0
while left < right:
    mid = (left + right) // 2
    ores_needed = make_fuel(mid)
    if ores_needed > num_ores:
        right = mid - 1
    else:
        max_fuel = mid
        left = mid + 1
print(max_fuel)