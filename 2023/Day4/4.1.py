import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

total = 0
for line in lines:
    card_data = line.split(':')[1]
    winning, nums = card_data.strip().split('|')
    winning = winning.strip().split(' ')
    winning = set([int(x) for x in winning if x.isnumeric()])
    nums = nums.strip().split(' ')
    nums = [int(x) for x in nums if x.isnumeric()]
    score = 0
    for num in nums:
        if num in winning:
            score = max(score*2, 1)
    total += score
print(total)