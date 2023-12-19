import sys
import networkx as nx

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

def get_neighbors(node):
    i,j = node
    neighbors = []
    dirs = pipe_data[grid[i][j]]
    for dir in dirs:
        if dir == 'left':
            i2 = i
            j2 = j - 1
            if 0 <= i2 < num_rows and 0 <= j2 < num_cols and grid[i2][j2] in rights:
                neighbors.append((i2,j2))
        elif dir == 'right':
            i2 = i
            j2 = j + 1
            if 0 <= i2 < num_rows and 0 <= j2 < num_cols and grid[i2][j2] in lefts:
                neighbors.append((i2,j2))
        elif dir == 'up':
            i2 = i - 1
            j2 = j
            if 0 <= i2 < num_rows and 0 <= j2 < num_cols and grid[i2][j2] in downs:
                neighbors.append((i2,j2))
        elif dir == 'down':
            i2 = i + 1
            j2 = j
            if 0 <= i2 < num_rows and 0 <= j2 < num_cols and grid[i2][j2] in ups:
                neighbors.append((i2,j2))
    return neighbors


if __name__ == '__main__':
    num_rows = len(grid)
    num_cols = len(grid[0])
    nodes = [(i,j) for i in range(num_rows) for j in range(num_cols)]
    start = (-1,-1)
    for node in nodes:
        if grid[node[0]][node[1]] == 'S':
            start = node
   
    pipe_data = {'-':['left', 'right'], '|':['up', 'down'], 'F':['right', 'down'], 'L':['right', 'up'], 'J':['left', 'up'], '7':['left', 'down'], '.':[]}
    rights = {'-', 'F', 'L'}
    lefts = {'-', 'J', '7'}
    ups = {'|', 'L', 'J'}
    downs = {'|', 'F', '7'}

    # Try all pipes to get desired cycle
    for pipe in pipe_data:
        grid[start[0]][start[1]] = pipe
        G = nx.Graph()
        G.add_nodes_from(nodes)
        for node in nodes:
            neighbors = get_neighbors(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        try:
            cycle = nx.find_cycle(G, source=start)
            print(f"Valid cycle when S is {pipe}")
            print(len(cycle) // 2)
            break
        except:
            pass