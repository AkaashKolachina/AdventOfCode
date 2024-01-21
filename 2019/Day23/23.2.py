import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

computers = [IntCode(program,[i]) for i in range(50)]
NAT = []
idle = set()
sent_by_nat = None
while True:
    for i in range(50):
        empty_queue = False
        if len(computers[i].input) < 2:
            computers[i].add_input(-1)
            empty_queue = True
        dest = computers[i].run()
        if dest is None and empty_queue:
            idle.add(i)
            continue
        elif dest is None:
            continue
        x = computers[i].run()
        y = computers[i].run()
        if dest == 255:
            NAT = [x,y]
            continue
        computers[dest].add_input(x)
        computers[dest].add_input(y)
    
    if len(idle) == 50:
        x,y = NAT
        if y == sent_by_nat:
            print(y)
            break
        sent_by_nat = y
        idle = set()
        computers[0].add_input(x)
        computers[0].add_input(y)