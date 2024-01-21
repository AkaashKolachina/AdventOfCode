import sys
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
input = [int(x) for x in data]

for _ in tqdm(range(100)):
    output = []
    for mult in range(1, len(input) + 1):
        pattern = [0] * mult + [1] * mult + [0] * mult + [-1] * mult
        i = 1
        out_elem = 0
        for num in input:
            out_elem += (num * pattern[i])
            i = (i + 1) % len(pattern)
        output.append(abs(out_elem) % 10)
    input = output

print(''.join([str(x) for x in input[:8]]))
