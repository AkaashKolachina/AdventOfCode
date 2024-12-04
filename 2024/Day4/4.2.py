import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'A':
            if 0 <= i - 1 and 0 <= j - 1 and i + 1 < len(grid) and j + 1 < len(grid[0]):
                set_1 = {grid[i + 1][j+1], grid[i-1][j-1]}
                set_2 = {grid[i - 1][j+1], grid[i+1][j-1]}
                if set_1 == set_2 and set_2 == {'M', 'S'}:
                    count += 1
print(count)