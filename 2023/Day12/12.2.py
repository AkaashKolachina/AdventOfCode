import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

rows = []
for line in lines:
    spring_str,blocks = line.split()
    blocks = [int(num) for num in blocks.split(',') if num.isnumeric()]
    springs = list(spring_str)
    springs = (springs + ['?']) * 5
    rows.append((springs[:-1],blocks * 5))
    
def dp(spring_idx, block_idx, cur_block_len):
    key = (spring_idx, block_idx, cur_block_len)
    if key in memo:
        return memo[key]
    
    if spring_idx == len(springs):
        if block_idx == len(blocks) and cur_block_len == 0:
            return 1
        elif block_idx == len(blocks) - 1 and cur_block_len == blocks[block_idx]:
            return 1
        else:
            return 0
    
    total = 0
    if springs[spring_idx] in ['?', '.']: 
        if cur_block_len == 0:
            total += dp(spring_idx + 1, block_idx, 0)
        elif block_idx < len(blocks) and cur_block_len == blocks[block_idx]:
            total += dp(spring_idx + 1, block_idx + 1, 0)
    if springs[spring_idx] in ['?', '#']:
        total += dp(spring_idx + 1, block_idx, cur_block_len + 1)
    
    memo[key] = total
    return total

combos = 0
for springs,blocks in rows:
    memo = {}
    combos += dp(0,0,0)
print(combos)