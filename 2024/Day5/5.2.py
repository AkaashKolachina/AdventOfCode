import sys
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]
rules = defaultdict(set)
pages = []
for line in lines:
    if line == '':
        continue
    if '|' in line:
        before,after = map(int,line.split('|'))
        rules[after].add(before)
    else:
        pages.append([int(x) for x in line.split(',')])

total = 0
for page in pages:
    is_right = True
    for i in range(len(page)):
        for j in range(i, len(page)):
            if page[j] in rules[page[i]]:
                is_right = False
                break
        if not is_right:
            break
    if not is_right:
        for i in range(len(page)):
            for j in range(i+1,len(page)):
                if page[j] in rules[page[i]]:
                    temp = page[j]
                    page[j] = page[i]
                    page[i] = temp
        total += page[len(page) //2]
print(total)