from sys import argv

def update_tail():
    if head_pos[0] == tail_pos[0]:
        #Same x val
        if abs(head_pos[1] - tail_pos[1]) > 1:
            if head_pos[1] > tail_pos[1]:
                tail_pos[1] += 1
                print("Move Right")
            else:
                tail_pos[1] -= 1
                print("Move Left")
        else:
            print("Did Nothing Boss")
    elif head_pos[1] == tail_pos[1]:
        if abs(head_pos[0] - tail_pos[0]) > 1:
            if head_pos[0] > tail_pos[0]:
                tail_pos[0] += 1
                print("Move Down")
            else:
                tail_pos[0] -= 1
                print("Move Up")
        else:
            print("Did Nothing Boss")
    elif abs(head_pos[1] - tail_pos[1]) > 1 or abs(head_pos[0] - tail_pos[0]) > 1:
        if abs(head_pos[0] - tail_pos[0]) > 1:
            if tail_pos[1] > head_pos[1]:
                if tail_pos[0] > head_pos[0]:
                    tail_pos[0] -= 1
                    tail_pos[1] -= 1
                else:
                    tail_pos[0] += 1
                    tail_pos[1] -= 1
            else:
                if tail_pos[0] > head_pos[0]:
                    tail_pos[0] -= 1
                    tail_pos[1] += 1
                else:
                    tail_pos[0] += 1
                    tail_pos[1] += 1
        else:
            if tail_pos[1] > head_pos[1]:
                if tail_pos[0] > head_pos[0]:
                    tail_pos[0] -= 1
                    tail_pos[1] -= 1
                else:
                    tail_pos[0] += 1
                    tail_pos[1] -= 1
            else:
                if tail_pos[0] > head_pos[0]:
                    tail_pos[0] -= 1
                    tail_pos[1] += 1
                else:
                    tail_pos[0] += 1
                    tail_pos[1] += 1
        print("Diag Action")
    else:
        print("Did Nothing Boss")

    print(head_pos)
    print(tail_pos)
    visited[(tail_pos[0], tail_pos[1])] = 1


def move(dir, num_moves):
    for i in range(num_moves):
        if dir == 'R':
            head_pos[1] += 1
        elif dir == 'L':
            head_pos[1] -= 1
        elif dir == 'U':
            head_pos[0] -= 1
        else:
            head_pos[0] += 1
        update_tail()

lines = []
with open(argv[1], "r") as f:
    lines = f.readlines()

visited = {}
head_pos = [20,20]
tail_pos = [20,20]

for line in lines:
    cmd = line.split(' ')
    move(cmd[0], int(cmd[1].strip()))
print(len(visited.items()))
