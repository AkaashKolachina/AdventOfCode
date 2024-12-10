import sys
from tqdm import tqdm
input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()

blocks = {}
spaces = []
idx = 0
greatest_id = 0

for i in range(len(data)):
    if i % 2 == 0:
        blocks[i // 2] = (idx, int(data[i]))
        greatest_id = i // 2
    else:
        spaces.append((idx, int(data[i])))
    idx += int(data[i])

while greatest_id >= 0:
    block_size = blocks[greatest_id][1]
    for i in range(len(spaces)):
        idx,space_size = spaces[i]
        if space_size >= block_size and blocks[greatest_id][0] > idx:
            blocks[greatest_id] = (idx,block_size)
            spaces[i] = (idx + block_size, space_size - block_size)
            if space_size == block_size:
                spaces.pop(i)
                i -= 1
            break
    greatest_id -= 1

checksum = 0
for id in blocks:
    idx,block_size = blocks[id]
    for inc in range(block_size):
        checksum += ((idx + inc) * id)
print(checksum)

