import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
wires = [[y for y in x.split(',')] for x in data.split('\n')]

dirs = {'R':(0,1), 'L':(0,-1), 'D':(-1,0), 'U': (1,0)}
visited = [set(), set()]
steps = [dict(), dict()]

for i in range(2):
    cur = (0,0)
    cur_steps = 0
    for step in wires[i]:
        dir = step[0]
        num_steps = int(step[1:])
        for _ in range(num_steps):
            cur = (cur[0] + dirs[dir][0], cur[1] + dirs[dir][1])
            cur_steps += 1
            visited[i].add(cur)
            if cur not in steps[i]:
                steps[i][cur] = cur_steps

intersections = visited[0].intersection(visited[1])
min_steps = float('inf')
for intersect in intersections:
    min_steps = min(min_steps, steps[0][intersect] + steps[1][intersect])
print(min_steps)