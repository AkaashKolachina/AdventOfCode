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
pixels = []

for cmd in cmds:
    pixel = (cycle - 1) % 40
    if abs(X - pixel) <= 1:
        pixels.append('#')
    else:
        pixels.append('.')

    c = cmd.split(' ')
    if c[0] == 'addx':
        X += int(c[1])
    cycle += 1

for i in range(0,len(pixels), 40):
    line = ''.join(pixels[i:i+40])
    print(line)

