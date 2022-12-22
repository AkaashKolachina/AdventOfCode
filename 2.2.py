from sys import argv

p1_map = {"A" : "R", "B" : "P", "C" : "S"}
score_map = {"R" : 1, "P" : 2, "S" : 3}

def get_outcome(p1,goal):
    if goal == "Y":
        return score_map[p1] + 3
    elif goal == "Z":
        if p1 == "R":
            return score_map["P"] + 6
        elif p1 == "P":
            return score_map["S"] + 6
        else:
            return score_map["R"] + 6
    else:
        if p1 == "R":
            return score_map["S"]
        elif p1 == "P":
            return score_map["R"] 
        else:
            return score_map["P"]

with open(argv[1], "r") as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        p1_move = p1_map[line[0]]
        goal = line[2]
        score += get_outcome(p1_move,goal)
    print(score)