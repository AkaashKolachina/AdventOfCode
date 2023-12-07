from sys import argv

def process(lines):
    cmds = []
    for line in lines:
        cmds.append('noop')
        if line.strip() != 'noop':
            cmds.append(line.strip())
    return cmds

lines = []
with open(argv[1], "r") as f:
    lines = f.readlines()

cmds = process(lines)

X = 1
cycle = 1
important_cycles = set([20,60,100,140,180,220])
sig_str_sum = 0

for cmd in cmds:
    if cycle in important_cycles:
        sig_str = cycle * X
        print("At cycle {} the signal strength is {}".format(cycle,sig_str))
        sig_str_sum += sig_str
    c = cmd.split(' ')
    if c[0] == 'addx':
        X += int(c[1])
    cycle += 1
print(sig_str_sum)
