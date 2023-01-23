from sys import argv
from tqdm import tqdm


def gen_piece(piece, height):
    y = height + 4
    if piece == 0:
        return set([(i,y) for i in range(2,6)])
    elif piece == 1:
        return set([(2,y+1),(3,y+1),(3,y+2),(3,y),(4,y+1)]) 
    elif piece == 2:
        return set([(2,y),(3,y),(4,y),(4,y+2),(4,y+1)])
    elif piece == 3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    else:
        return set([(2,y),(2,y+1),(3,y),(3,y+1)])

def move_x(piece, dx):
    can_move = True
    for part in piece:
        if part[0] + dx >= 7 or part[0] + dx < 0 or (part[0] + dx, part[1]) in rocks:
            can_move = False
            break
    if can_move:
        return set([(x + dx,y) for (x,y) in piece])
    else:
        return piece

pattern = open(argv[1]).read().strip()
moves = {'<': -1, '>': 1}
pieces = [i for i in range(5)]
rocks = set([(i,0) for i in range(7)]) # Add floor
height = 0
i = 0
j = 0
found_cycle = False
move_log = {}
num_pieces = 0
cycle_height = 0
cycle_size = 0
start_key = ()
dhs = []
while not found_cycle:
    i %= len(pieces)
    piece = gen_piece(pieces[i],height)
    has_stopped = False
    while not has_stopped:
        j %= len(pattern)
        move = pattern[j]
        j += 1
        piece = move_x(piece,moves[move])
        for part in piece:
            if (part[0], part[1] - 1) in rocks:
                has_stopped = True
                break
        if not has_stopped:
            piece = set([(x,y - 1) for (x,y) in piece])
    rocks |= piece
    i += 1
    num_pieces += 1
    old_height = height
    height = max(height,max([y for (x,y) in piece]) )
    dh = height - old_height
    dhs.append(dh)
    key = (i,j,dh)
    if key in move_log:
        found_cycle = True
        start_key = key
        cycle_height = height - move_log[key][0]
        cycle_size = num_pieces - move_log[key][1]

    else:
        move_log[key] = (height, num_pieces)

#print(start_key,cycle_height,cycle_size)
start_height = move_log[start_key][0] - start_key[-1]
start_pieces = move_log[start_key][1] - 1
num_cycles = (1000000000000 - start_pieces) // cycle_size
rem = (1000000000000 - start_pieces) % cycle_size
total = start_height + (num_cycles * cycle_height)
total += sum(dhs[start_pieces:start_pieces+rem])

print(total)
