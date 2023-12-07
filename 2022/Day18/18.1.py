from sys import argv

data = open(argv[1]).read().strip()
lines = [x for x in data.split('\n')]

drops = set()

for line in lines:
    coords = tuple(int(coord) for coord in line.split(','))
    drops.add(coords)

sa = 0
get_neighbors = lambda x,y,z : [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]

for coords in drops:
    sides = 6
    neighbors = get_neighbors(*coords)
    for neighbor in neighbors:
        if neighbor in drops:
            sides -= 1
    
    sa += sides

print(sa)

