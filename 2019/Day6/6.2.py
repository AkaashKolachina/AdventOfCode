import sys
from collections import deque, defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

orbits = {}
orbited_by = defaultdict(list)
for line in lines:
    ob1,ob2 = line.split(')')
    orbits[ob2] = ob1
    orbited_by[ob1].append(ob2)

start = orbits['YOU']
end = orbits['SAN']
visited = set()
q = deque([(start, 0)])

while q:
    object, num_transfers = q.pop()
    if object in visited:
        continue
    visited.add(object)

    if object == end:
        print(num_transfers)
        break
    if object in orbits:
        q.appendleft((orbits[object], num_transfers + 1))
    for nb in orbited_by[object]:
        q.appendleft((nb, num_transfers + 1))