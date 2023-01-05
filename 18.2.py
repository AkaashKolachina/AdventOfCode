from sys import argv

data = open(argv[1]).read().strip()
lines = [x for x in data.split('\n')]

drops = set()
min_x,min_y,min_z = float('inf'),float('inf'),float('inf')
max_x,max_y,max_z = float('-inf'),float('-inf'),float('-inf')
get_neighbors = lambda x,y,z : [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]

for line in lines:
    coords = tuple(int(coord) for coord in line.split(','))
    drops.add(coords)

    min_x = min(min_x, coords[0])
    max_x = max(max_x,coords[0])
    min_y = min(min_y, coords[1])
    max_y = max(max_y,coords[1])
    min_z = min(min_z, coords[2])
    max_z = max(max_z,coords[2])

sa = 0
s = [(min_x - 1, min_y - 1, min_z - 1)]
visited = set()
mins = (min_x -1,min_y-1,min_z-1)
maxs = (max_x + 1,max_y + 1,max_z + 1)
sa = 0
while s:
    point = s.pop()
    if point in visited:
        continue
    visited.add(point)
    neighbors = get_neighbors(*point)
    for neighbor in neighbors:
        if neighbor not in drops:
            in_bounds = True
            for i in range(3):
                if neighbor[i] < mins[i] or neighbor[i] > maxs[i]:
                    in_bounds = False
                    break
            if in_bounds:
                s.append(neighbor)
        else:
            sa += 1

print(sa)



