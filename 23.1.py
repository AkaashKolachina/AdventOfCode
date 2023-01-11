from sys import argv
from collections import defaultdict

elves = set()
data = open(argv[1]).read().strip().split('\n')
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            elves.add((i,j))

dirs = [(-1,0), (1,0), (0,-1), (0,1)]
all_dirs = {}
all_dirs[(0,-1)] = [(0,-1), (1,-1), (-1,-1)]
all_dirs[(0,1)] = [(0,1), (1,1), (-1,1)]
all_dirs[(-1,0)] = [(-1,0), (-1,1), (-1,-1)]
all_dirs[(1,0)] = [(1,0), (1,-1), (1,1)]

for _ in range(10):
    moves = defaultdict(list)
    # Stage 1
    for elf in elves:
        (x,y) = elf
        coords = [-1,0,1]
        all_clear = True
        for i in coords:
            for j in coords:
                if (i,j) != (0,0) and (x + i, y + j) in elves:
                    all_clear = False
                    break
        if all_clear:
            continue
        proposed_move = False
        for dir in dirs:
            if proposed_move:
                break
            for (dx,dy) in all_dirs[dir]:
                has_elf = False
                if (x + dx, y + dy) in elves:
                    has_elf = True
                    break
            if not has_elf:
                moves[(x + dir[0], y + dir[1])].append(elf)
                proposed_move = True
    # Stage 2
    for dest,origins in moves.items():
        if len(origins) == 1:
            elves.remove(origins[0])
            elves.add(dest)

    dir = dirs[0]
    dirs.remove(dir)
    dirs.append(dir)

xs = [x for (x,y) in elves]
ys = [y for (x,y) in elves]
spaces = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
rocks = spaces - len(elves)
print(rocks)