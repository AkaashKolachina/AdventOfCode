import operator
from sys import argv
from math import floor
import numpy as np

class Monkey:
    def __init__(self,items, term_1, term_2, op, test_num, true_monkey, fail_monkey):
        self.items = items
        self.term_1 = term_1
        self.term_2 = term_2
        self.op = op
        self.test_num = test_num
        self.true_monkey = true_monkey
        self.fail_monkey = fail_monkey 
    
    def inspect(self,item,lcm):
        ops = { "+": operator.add, "*": operator.mul}
        p2 = 0
        if self.term_2 == 'old':
            p2 = item
        else:
            p2 = int(self.term_2)
        
        item %= lcm
        p2 %= lcm
        new = ops[self.op](item,p2)
        return new
    
    def toss(self,item):
        if item % self.test_num == 0:
            return self.true_monkey
        else:
            return self.fail_monkey
    

lines = []
with open(argv[1], "r") as f:
    lines = f.readlines()

monkeys = []
for i in range(0,len(lines), 7):
    # Parse Items
    input = lines[i+1].split(':')[1].strip()
    items = input.split(', ')
    items = [int(item) for item in items]

    # Parse Function
    function = lines[i+2].split(':')[1].strip()
    components = function.split(' ')
    term_1 = components[2]
    term_2 = components[4]
    op = components[3]

    # Throw data
    test_num = int(lines[i+3].split(' ')[-1].strip())
    true_monkey = int(lines[i+4].split(' ')[-1].strip())
    fail_monkey = int(lines[i+5].split(' ')[-1].strip())

    monkeys.append(Monkey(items, term_1, term_2, op, test_num, true_monkey, fail_monkey))

inspect_counts = []
div_nums = []
for i,monkey in enumerate(monkeys):
    inspect_counts.append(0)
    div_nums.append(monkey.test_num)
lcm = np.lcm.reduce(div_nums)
for _ in range(10000):
    for i in range(len(monkeys)):
        while len(monkeys[i].items) != 0:
            item = monkeys[i].items.pop(0)
            item = monkeys[i].inspect(item,lcm)
            inspect_counts[i] += 1
            toss_idx = monkeys[i].toss(item)
            monkeys[toss_idx].items.append(item)

inspect_counts.sort(reverse = True)
print(inspect_counts)
print(inspect_counts[0] * inspect_counts[1])
