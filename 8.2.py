from sys import argv
import numpy as np


def get_score(tree, trees):
    score = 0
    for t in trees:
        score += 1
        if t >= tree:
            break
    return score

with open(argv[1], "r") as f:
    lines = f.readlines()
    n = len(lines)
    m = len(lines[0].strip())
    for i in range(n):
        lines[i] = [int(s) for s in lines[i].strip()]
    lines = np.array(lines)
    best_score = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            left = lines[i][:j][::-1]
            right = lines[i][j + 1:]
            up = lines[:i,j][::-1]
            down = lines[i + 1:,j]
            score = get_score(lines[i][j], up) * get_score(lines[i][j], down) * get_score(lines[i][j], left) * get_score(lines[i][j], right)
            if score > best_score:
                best_score = score

    print(best_score)