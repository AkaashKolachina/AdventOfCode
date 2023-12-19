import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
universe = [list(x) for x in data.split('\n')]
num_rows = len(universe)
num_cols = len(universe[0])

galaxies = []
for i in range(num_rows):
    for j in range(num_cols):
        if universe[i][j] == '#':
            galaxies.append((i,j))

empty_rows = {i for i in range(num_rows) if all([elem == '.' for elem in universe[i]])}
universe_t = list(zip(*universe))
empty_cols = {i for i in range(num_cols) if all([elem == '.' for elem in universe_t[i]])}

def weight(point):
    i,j = point
    return 1000000 if i in empty_rows or j in empty_cols else 1

total = 0
for i in range(len(galaxies)):
    for j in range(i,len(galaxies)):
        col = galaxies[i][1]
        total += sum([weight((row,col)) for row in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0]))])

        row = galaxies[i][0]
        total += sum([weight((row,col)) for col in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1]))])
print(total)