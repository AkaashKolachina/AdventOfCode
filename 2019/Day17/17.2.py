import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

ic = IntCode(program.copy())
grid = [[]]

has_halted = False
while not has_halted:
    output = ic.run()
    if output is None:
        has_halted = True
        break
    if output == 10:
        grid.append([])
    else:
        grid[-1].append(chr(output))

grid = grid[:grid.index([])]
dirs = [(0,1), (1,0),(0,-1), (-1,0)]

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] =='^':
            start = (i,j)
            break
    if start is not None:
        break

path = []
dir_idx = 3
cur = start
while True:
    new_pos = (cur[0] + dirs[dir_idx][0], cur[1] + dirs[dir_idx][1])
    count = 0
    while 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] != '.':
        count += 1
        cur = new_pos
        new_pos = (cur[0] + dirs[dir_idx][0], cur[1] + dirs[dir_idx][1])

    if count > 0:
        path.append(str(count))
    new_dir_idx = (dir_idx + 1) % len(dirs)
    new_pos = (cur[0] + dirs[new_dir_idx][0], cur[1] + dirs[new_dir_idx][1])
    if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] != '.':
        path.append('R')
        dir_idx = new_dir_idx
        continue
    new_dir_idx = (dir_idx - 1) % len(dirs)
    new_pos = (cur[0] + dirs[new_dir_idx][0], cur[1] + dirs[new_dir_idx][1])
    if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] != '.':
        path.append('L')
        dir_idx = new_dir_idx
        continue
    break

path = list(zip(path[::2], path[1::2]))
A = ','.join(['R', '10', 'R', '10', 'R', '6', 'R', '4'])
B = ','.join(['R', '10', 'R', '10', 'L', '4'])
C = ','.join(['R', '4', 'L', '4', 'L', '10', 'L', '10'])
main = ','.join(['A','B','A','C','A','B','C','B','C','B'])

program[0] = 2
input = '\n'.join([main,A,B,C,'n\n'])
input = [ord(i) for i in input]
ic = IntCode(program,input)
has_halted = False
while not has_halted:
    out = ic.run()
    if out is None:
        has_halted = True
    else:
        if out > 255:
            print(out)