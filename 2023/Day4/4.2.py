import sys
import re
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

card_counts = defaultdict(int)
for line in lines:
    card_id,card_data = line.split(':')
    card_id = int(re.search(r'\d+', card_id).group())
    card_counts[card_id] += 1
    winning, nums = card_data.strip().split('|')
    winning = winning.strip().split(' ')
    winning = set([int(x) for x in winning if x.isnumeric()])
    nums = nums.strip().split(' ')
    nums = [int(x) for x in nums if x.isnumeric()]

    num_wins = 0
    for num in nums:
        if num in winning:
            num_wins += 1
    
    for i in range(1, 1 + num_wins):
        # Add 1 for each card
        card_counts[card_id + i] += card_counts[card_id]

print(sum(card_counts.values()))