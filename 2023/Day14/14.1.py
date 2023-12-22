import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
rock_grid = [list(x) for x in data.split('\n')]

# Move rocks up
for i in range(1,len(rock_grid)):
    row = rock_grid[i]
    for rock_idx,rock in enumerate(row):
        if rock == 'O':
            j = i - 1
            while j >= 0:
                if rock_grid[j][rock_idx] == '.':
                    rock_grid[j + 1][rock_idx] = '.'
                    rock_grid[j][rock_idx] = 'O'
                    j -= 1
                else:
                    break


total = 0
for i,row in enumerate(rock_grid):
    total += (len(rock_grid) - i) * ''.join(row).count('O')
print(total)
