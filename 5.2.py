from sys import argv

stacks = []
for i in range(9):
    stacks.append([])

with open(argv[1], "r") as f:
    lines = f.readlines()
    idx = 1
    for stack_idx in range(9):
        i = 7
        while i >= 0:
            letter = lines[i][idx]
            if letter.isalpha():
                stacks[stack_idx].append(letter)
            i -= 1
        idx += 4
    
    lines = lines[10:]
    for line in lines:
        words = line.split(' ')
        num_pops = int(words[1])
        src = int(words[3]) - 1
        dest = int(words[5]) - 1
        imd = []
        for i in range(num_pops):
            imd.append(stacks[src].pop())
        for i in range(num_pops):
            stacks[dest].append(imd.pop())
    
    res = ""
    for i in range(9):
        res += stacks[i].pop()
    print(res)