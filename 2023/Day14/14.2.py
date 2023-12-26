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

def move_west():
    for row in rock_grid:
        i = 1
        while i < len(row):
            if row[i] == 'O':
                j = i - 1
                while j >= 0:
                    if row[j] == '.':
                        row[j + 1] = '.'
                        row[j] = 'O'
                        j -= 1
                    else:
                        break
                i += 1
            else:
                i += 1

def move_east():
    for row in rock_grid:
        i = len(row) - 2
        while i >= 0:
            if row[i] == 'O':
                j = i + 1
                while j < len(row):
                    if row[j] == '.':
                        row[j - 1] = '.'
                        row[j] = 'O'
                        j += 1
                    else:
                        break
                i -= 1
            else:
                i -= 1

def cycle():
    move_north()
    move_west()
    move_south()
    move_east()

def freeze(grid):
    return tuple([tuple(row) for row in grid])

num_spins = 1000000000
states = {}
cycle_found = False
t = 1
start = -1
while not cycle_found:
    cycle()
    state = freeze(rock_grid)
    if state not in states:
        states[state] = t
        t += 1 
    else:
        cycle_found = True
        start = states[state]

cycle_length = t - start
num_cycles = (num_spins - start) // cycle_length

# Probably could just optimize by finding state in states instead of cycling more
for _ in range(start + num_cycles * cycle_length, num_spins):
    cycle()



total = 0
for i,row in enumerate(rock_grid):
    total += (len(rock_grid) - i) * ''.join(row).count('O')
print(total)
