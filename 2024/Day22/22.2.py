import sys
from collections import defaultdict
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [int(x) for x in data.split('\n')]

mod_num = 16777216

def get_next_secret(num):
    secret = (num ^ (num*64)) % mod_num
    result = secret // 32
    secret ^= result
    secret %= mod_num
    result = secret * 2048
    secret ^= result
    secret %= mod_num
    return secret

sequence_sums = defaultdict(int)
for num in tqdm(lines):
    seen = set()
    secret = num
    prices = [secret % 10]
    for _ in range(2000):
        secret = get_next_secret(secret)
        prices.append(secret % 10)
    
    diffs = [prices[i] - prices[i-1] for i in range(1,len(prices))]
    for i in range(len(diffs) - 3):
        sequence = (diffs[i], diffs[i+1], diffs[i+2], diffs[i+3])
        if sequence not in seen:
            sequence_sums[sequence] += prices[i+4]
            seen.add(sequence)

print(max(sequence_sums.values()))