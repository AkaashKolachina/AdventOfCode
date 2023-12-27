import sys
from operator import lt, gt

ops = {'<':lt, '>':gt}

def is_accepted(part, workflow):
    if workflow in ['A','R']:
        return workflow == 'A'
    for rule in workflows[workflow]:
        if ':' not in rule:
            if rule in workflows:
                return is_accepted(part, rule)
            else:
                return rule == 'A'
        else:
            cond,to_ret = rule.split(':')
            key = cond[0]
            op = cond[1]
            num = int(cond[2:])
            if ops[op](part[key], num):
                return is_accepted(part, to_ret)

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]
split_idx = lines.index('')
workflow_array = lines[:split_idx]
parts_array = lines[split_idx + 1:]

workflows = {}
parts = []

for line in workflow_array:
    name, rest = line.split('{')
    rest = rest.strip()[:-1]
    workflows[name] = []
    for rule in rest.split(','):
        workflows[name].append(rule)

for line in parts_array:
    vars = line.strip()[1:-1]
    part = {}
    for var in vars.split(','):
        var_name,var_val = var.split('=')
        part[var_name] = int(var_val)
    parts.append(part)

accepted_sum = 0
start = 'in'
for part in parts:
    if is_accepted(part, start):
        accepted_sum += sum(part.values())
print(accepted_sum)