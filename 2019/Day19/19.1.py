import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

grid = [['.' for i in range(50)] for j in range(50)]
affected = 0
for x in range(50):
    for y in range(50):
        ic = IntCode(program.copy(), [x,y])
        is_affected = ic.run() == 1
        affected += 1 if is_affected else 0
        if is_affected:
            grid[y][x] = '#'
print(affected)
for line in grid:
    print(''.join(line))