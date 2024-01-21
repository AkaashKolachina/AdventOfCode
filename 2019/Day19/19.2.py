import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]


x = 0
y = 0
while True:
    output = IntCode(program.copy(),[x+99,y]).run()
    if output:
        break
    y += 1
    while True:
        output = IntCode(program.copy(),[x,y+99]).run()
        if output:
            break
        x += 1
print(x*10000+y)
    
