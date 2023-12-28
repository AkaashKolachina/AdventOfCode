import sys
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

neighbors = {}
flip_flops = {}
conjunctions = {}

for line in lines:
    node, nbs = line.split('->')
    node = node.strip()
    nbs = nbs.strip()
    if node[0] == '%':
        node = node[1:]
        flip_flops[node] = False # Default to off
    elif node[0] == '&':
        node = node[1:]
        conjunctions[node] = {}
    neighbors[node] = [nb.strip() for nb in nbs.split(',')]

for node in neighbors:
    for nb in neighbors[node]:
        if nb in conjunctions:
            conjunctions[nb][node] = False

# False -> low pulse
# True - high pulse
num_lows = 0
num_highs = 0

for _ in range(1000):
    start = ('broadcaster', 'button', False)
    q = deque([start])
    while q:
        node, parent, pulse = q.pop()
        if pulse:
            num_highs += 1
        else:
            num_lows += 1
        if node in flip_flops:
            if not pulse:
                flip_flops[node] = not flip_flops[node]
                new_pulse = flip_flops[node]
                for nb in neighbors.get(node, []):
                    q.appendleft((nb, node, new_pulse))
        elif node in conjunctions:
            conjunctions[node][parent] = pulse
            new_pulse = not all(conjunctions[node].values())
            for nb in neighbors.get(node, []):
                q.appendleft((nb, node, new_pulse))
        else:
            for nb in neighbors.get(node, []):
                q.appendleft((nb, node, pulse))

print(num_lows * num_highs)