from sys import argv
import numpy as np

with open(argv[1], "r") as f:
    lines = f.readlines()
    n = len(lines)
    m = len(lines[0].strip())
    for i in range(n):
        lines[i] = [int(s) for s in lines[i].strip()]
    lines = np.array(lines)
 
    visible = (2 * n) + (2 * m) - 4
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            left = lines[i][:j]
            right = lines[i][j + 1:]
            up = lines[:i,j]
            down = lines[i + 1:,j]
            if lines[i][j] > np.max(up) or lines[i][j] > np.max(down) or lines[i][j] > np.max(left) or lines[i][j] > np.max(right):
                visible += 1 

    print(visible)