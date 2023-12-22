import sys
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
rock_grid = [list(x) for x in data.split('\n')]

def move_north():
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

def move_south():
    for i in range(len(rock_grid) - 2, -1 ,-1):
        row = rock_grid[i]
        for rock_idx,rock in enumerate(row):
            if rock == 'O':
                j = i + 1
                while j < len(rock_grid):
                    if rock_grid[j][rock_idx] == '.':
                        rock_grid[j - 1][rock_idx] = '.'
                        rock_grid[j][rock_idx] = 'O'
                        j += 1
                    else:
                        break

def move_east():
    for row in rock_grid:
        i = 0
        while i < len(row) - 1:
            if row[i] == 'O':
                j = i + 1
                while j < len(row):
                    if row[j] == '.':
                        row[j - 1] = '.'
                        row[j] = 'O'
                        j += 1
                    else:
                        break
                i = j
            else:
                i += 1

def move_west():
    for row in rock_grid:
        i = len(row) - 1
        while i >= 0:
            if row[i] == 'O':
                j = i - 1
                while j >= 0:
                    if row[j] == '.':
                        row[j + 1] = '.'
                        row[j] = 'O'
                        j -= 1
                    else:
                        break
                i = j
            else:
                i -= 1

def cycle():
    move_north()
    move_west()
    move_south()
    move_east()

for _ in tqdm(range(5)):
    cycle()
    print()
    for row in rock_grid:
        print(row)




total = 0
for i,row in enumerate(rock_grid):
    total += (len(rock_grid) - i) * ''.join(row).count('O')
print(total)
