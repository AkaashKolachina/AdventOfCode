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
for _ in range(2022):
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
    height = max(height,max([y for (x,y) in piece]) )

print(height)

