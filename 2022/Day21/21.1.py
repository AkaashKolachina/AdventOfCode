from sys import argv
import operator

ops = { "+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.floordiv}

data = open(argv[1]).read().strip().split('\n')
lines = [x for x in data]
monkeys = {}


def get_num(monkey):
    if isinstance(monkeys[monkey],int):
        return monkeys[monkey]
    else:
        (p1,op,p2) = monkeys[monkey]
        monkeys[monkey] = ops[op](get_num(p1),get_num(p2))
        return monkeys[monkey]

for line in lines:
    monkey, val = line.split(':')
    if val.strip().isnumeric():
        monkeys[monkey.strip()] = int(val.strip())
    else:
        parts = val.strip().split(' ')
        monkeys[monkey.strip()] = tuple([part for part in parts])

print(get_num('root'))