import sys
import heapq

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [[int(x) for x in row] for row in data.split('\n')]


RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)
dirs = [RIGHT,DOWN,LEFT,UP]

def get_neighbors(state):
    neighbors = []
    cost, (i,j), cur_dir_idx = state

    # Turn right
    new_dir_idx = (cur_dir_idx + 1) % 4
    new_dir = dirs[new_dir_idx]
    new_cost = cost
    for step in range(1,11):
        i2 = i + new_dir[0] * step
        j2 = j + new_dir[1] * step
        if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]):
            new_cost += grid[i2][j2]
            if step >= 4:
                neighbors.append((new_cost, (i2,j2), new_dir_idx))

    # Turn left
    new_dir_idx = (cur_dir_idx - 1) % 4
    new_dir = dirs[new_dir_idx]
    new_cost = cost
    for step in range(1,11):
        i2 = i + new_dir[0] * step
        j2 = j + new_dir[1] * step
        if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]):
            new_cost += grid[i2][j2]
            if step >= 4:
                neighbors.append((new_cost, (i2,j2), new_dir_idx))
    return neighbors



start = (0,0)
end = (len(grid) - 1, len(grid[0]) - 1)
pq = [(0,(0,0),i) for i in range(4)]
costs = {}
prev = {start:None}

while pq:
    state = heapq.heappop(pq)
    cost, (i,j), cur_dir_idx = state

    if (i,j) == end:
        print(cost)
        break

    neighbors = get_neighbors(state)
    for nb_state in neighbors:
        nb_cost, nb_pos, dir_idx = nb_state
        if (nb_pos, dir_idx) not in costs or costs[(nb_pos, dir_idx)] > nb_cost:
            costs[(nb_pos, dir_idx)] = nb_cost
            heapq.heappush(pq,nb_state)


