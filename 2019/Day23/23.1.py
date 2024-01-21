import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

computers = [IntCode(program,[i]) for i in range(50)]
found = False
while not found:
    for i in range(50):
        if len(computers[i].input) < 2:
            computers[i].add_input(-1)
        dest = computers[i].run()
        if dest is None:
            continue
        x = computers[i].run()
        y = computers[i].run()
        if dest == 255:
            print(y)
            found = True
            break
        computers[dest].add_input(x)
        computers[dest].add_input(y)