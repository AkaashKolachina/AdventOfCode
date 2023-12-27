import sys
from copy import deepcopy
    
input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]
workflow_array = lines[:lines.index('')]
total_combos = 0

workflows = {}
for line in workflow_array:
    name, rest = line.split('{')
    rest = rest.strip()[:-1]
    workflows[name] = []
    for rule in rest.split(','):
        workflows[name].append(rule)

def backtrack(cur_bounds, workflow):
    if workflow == 'A':
        # Calc combos that go through this path
        num_combos = 1
        for bound in cur_bounds.values():
            num_combos *= (bound[1] - bound[0])
        global total_combos
        total_combos += num_combos
    elif workflow == 'R':
        return
    else:
        for rule in workflows[workflow]:
            if ':' not in rule:
               backtrack(cur_bounds, rule)
            else:
                new_bounds = deepcopy(cur_bounds)
                cond,to_ret = rule.split(':')
                key = cond[0]
                op = cond[1]
                num = int(cond[2:])
                if op == '<':
                    new_bounds[key][1] = num
                    cur_bounds[key][0] = num 
                else:
                    new_bounds[key][0] = num + 1
                    cur_bounds[key][1] = num + 1
                backtrack(new_bounds, to_ret)


start = 'in'
bounds = {}
for key in ['x', 'm', 'a', 's']:
    bounds[key] = [1,4001]
backtrack(bounds,start)
print(total_combos)