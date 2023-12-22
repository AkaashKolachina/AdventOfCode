import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
sequence = [x for x in data.split(',')]

total = 0
for seq in sequence:
    cur_val = 0
    for c in seq:
        cur_val += ord(c)
        cur_val *= 17
        cur_val %= 256
    total += cur_val
print(total)