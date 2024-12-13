import sys
import re
from z3 import *

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

machines = []

for i in range(0,len(lines),4):
    machine = []
    for inc in range(3):
        x,y = map(int, re.findall(r"\d+",lines[i + inc]))
        machine.append((x,y))
    machines.append(machine)


total_price = 0
for machine in machines:
    A,B,prize = machine
    x_a,y_a = A
    x_b,y_b = B
    x_p,y_p = prize

    a = Int('a')
    b = Int('b')
    s = Solver()
    s.add(a*x_a + b*x_b == x_p)
    s.add(a*y_a + b*y_b == y_p)
    if s.check() == sat:
        model = s.model()
        num_a = model[a].as_long()
        num_b = model[b].as_long()
        total_price += (3*num_a + num_b)
print(total_price)
