from sys import argv

def update_tail(i,j):
    head_pos = pos[i]
    tail_pos = pos[j]
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

    #print(head_pos)
    #print(tail_pos)
    if j == 9:
        visited[(tail_pos[0], tail_pos[1])] = 1


def update():
    for i in range(len(pos) - 1):
        update_tail(i, i+ 1)


def move(dir, num_moves):
    for i in range(num_moves):
        if dir == 'R':
            pos[0][1] += 1
        elif dir == 'L':
            pos[0][1] -= 1
        elif dir == 'U':
            pos[0][0] -= 1
        else:
            pos[0][0] += 1
        update()

lines = []
with open(argv[1], "r") as f:
    lines = f.readlines()

visited = {}
pos = []
for i in range(20):
    pos.append([20,20])

for line in lines:
    cmd = line.split(' ')
    move(cmd[0], int(cmd[1].strip()))
print(len(visited.items()))
