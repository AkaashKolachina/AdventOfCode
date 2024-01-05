import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
wires = [[y for y in x.split(',')] for x in data.split('\n')]

dirs = {'R':(0,1), 'L':(0,-1), 'D':(-1,0), 'U': (1,0)}
visited = [set(), set()]

for i in range(2):
    cur = (0,0)
    for step in wires[i]:
        dir = step[0]
        num_steps = int(step[1:])
        for _ in range(num_steps):
            cur = (cur[0] + dirs[dir][0], cur[1] + dirs[dir][1])
            visited[i].add(cur)

intersections = visited[0].intersection(visited[1])
min_x,min_y = min(intersections, key = lambda coord: abs(coord[0]) + abs(coord[1]))
print(abs(min_x) + abs(min_y))