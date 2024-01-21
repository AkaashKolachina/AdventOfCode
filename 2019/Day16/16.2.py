import sys
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
input = [int(x) for x in data]

offset = int(''.join([str(x) for x in input[:7]]))
rem = input[(offset % len(input)):]
num_copies = ((len(input) * 10000) - (len(rem) + offset)) // len(input)
expanded_input = input * num_copies
expanded_input = rem + expanded_input

for _ in tqdm(range(100)):
    acc = 0
    for i in range(len(expanded_input) - 1,-1,-1):
        acc += expanded_input[i]
        expanded_input[i] = (acc % 10)
print(''.join([str(x) for x in expanded_input[:8]]))