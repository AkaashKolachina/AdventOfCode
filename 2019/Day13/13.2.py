import sys
sys.path.append('..')
from intcode import IntCode
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]
program[0] = 2

tiles = defaultdict(int)
ic = IntCode(program.copy())

#Tile Types
EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

# Joystick Inputs
NEUTRAL = 0
LEFT = -1
RIGHT = 1

SCORE_MODE = (-1,0)

has_halted = False
update_input = False
ball = None
paddle = None
score = 0
while not has_halted:
    tile_data = []
    for _ in range(3):
        tile_data.append(ic.run())
    if None in tile_data:
        has_halted = True
        break
    x,y,t = tile_data
    if t == BALL:
        update_input = True
        ball = (x,y)
    elif t == PADDLE:
        update_input = True
        paddle = (x,y)
    elif (x,y) == SCORE_MODE:
        score = t
    
    if update_input and ball is not None and paddle is not None:
        if ball[0] < paddle[0]:
            ic.input = [LEFT]
        elif ball[0] > paddle[0]:
            ic.input = [RIGHT]
        else:
            ic.input = [NEUTRAL]
        update_input = False

print(score)