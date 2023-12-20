import sys
import re
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

rows = []
for line in lines:
    spring_str,key = line.split()
    key = [int(num) for num in key.split(',') if num.isnumeric()]
    springs = list(spring_str)
    question_idxs = [i for i,spring in enumerate(springs) if spring == '?']
    rows.append((springs,key,question_idxs))

def is_valid(spring_str, key):
    blocks = [len(block) for block in re.findall(r'\#+', spring_str)]
    return blocks == key

def backtrack(cur_row, key, question_idxs, results):
    if len(question_idxs) == 0:
        spring_str = ''.join(cur_row)
        if is_valid(spring_str,key):
            results.append(spring_str)
    else:
        for symbol in ['#', '.']:
            new_row = cur_row[:]
            new_row[question_idxs[0]] = symbol
            backtrack(new_row, key, question_idxs[1:],results)

total = 0
for row in tqdm(rows):
    springs,key,question_idxs = row
    results = []
    backtrack(springs, key, question_idxs,results)
    total += len(results)
print(total)