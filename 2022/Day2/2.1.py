from sys import argv

p1_map = {"A" : "R", "B" : "P", "C" : "S"}
p2_map = {"X" : "R", "Y" : "P", "Z" : "S"}
score_map = {"R" : 1, "P" : 2, "S" : 3}

def get_outcome(p1,p2):
    if p1 == p2:
        return 3
    
    if (p1 == "R" and p2 == "P") or (p1 == "S" and p2 == "R") or (p1 == "P" and p2 == "S"):
        return 6
    else:
        return 0

with open(argv[1], "r") as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        p1_move = p1_map[line[0]]
        p2_move = p2_map[line[2]]
        score += score_map[p2_move] + get_outcome(p1_move,p2_move)
    print(score)