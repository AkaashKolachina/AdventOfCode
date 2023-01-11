from sys import argv
import operator
import sympy
from sympy.parsing.sympy_parser import parse_expr

ops = { "+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.floordiv}

data = open(argv[1]).read().strip().split('\n')
lines = [x for x in data]
monkeys = {}


def get_expr(monkey):
    if not isinstance(monkeys[monkey],tuple):
        return monkeys[monkey]
    else:
        (p1,op,p2) = monkeys[monkey]
        monkeys[monkey] = "({} {} {})".format(get_expr(p1), op, get_expr(p2))
        return monkeys[monkey]

for line in lines:
    monkey, val = line.split(':')
    if val.strip().isnumeric():
        monkeys[monkey.strip()] = val.strip()
    else:
        parts = val.strip().split(' ')
        monkeys[monkey.strip()] = tuple([part for part in parts])
monkeys['humn'] = 'x'
expr = get_expr(monkeys['root'][0]) + ' - ' + get_expr(monkeys['root'][2])
print(expr)
print(sympy.solvers.solve(expr,'x'))