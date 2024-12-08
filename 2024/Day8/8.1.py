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
        for j in range(i+1, len(antennas[antenna])):
            c,d = antennas[antenna][j]
            di = c - a
            dj = d - b

            if 0 <= a - di < len(grid) and 0 <= b - dj < len(grid[0]):
                antinodes.add((a-di,b-dj))
            if 0 <= c + di < len(grid) and 0 <= d + dj < len(grid[0]):
                antinodes.add((c+di,d+dj))
print(len(antinodes))
