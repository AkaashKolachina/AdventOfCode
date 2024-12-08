import sys
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

antennas = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            antennas[grid[i][j]].append((i,j))


antinodes = set()

for antenna in antennas:
    for i in range(len(antennas[antenna])):
        a,b = antennas[antenna][i]
        antinodes.add((a,b))
        for j in range(i+1, len(antennas[antenna])):
            c,d = antennas[antenna][j]
            antinodes.add((c,d))
            in_bounds = True
            di = c - a
            dj = d - b
            x = a
            y = b
            while in_bounds:
                if 0 <= x - di < len(grid) and 0 <= y - dj < len(grid[0]):
                    antinodes.add((x-di,y-dj))
                    x -= di
                    y -= dj
                else:
                    in_bounds = False

            in_bounds = True
            x = c
            y = d
            while in_bounds:
                if 0 <= x + di < len(grid) and 0 <= y + dj < len(grid[0]):
                    antinodes.add((x+di,y+dj))
                    x += di
                    y += dj
                else:
                    in_bounds = False
print(len(antinodes))
