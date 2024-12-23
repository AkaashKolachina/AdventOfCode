import sys
from operator import add, mul
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]
def concat(num1,num2):
    return int(str(num1) + str(num2))

ops = [add,mul,concat]
totals = set()
def backtrack(target, cur, i, nums):
    if i == len(nums):
        if cur == target:
            totals.add(target)
    elif cur > target:
        return
    else:
        for op in ops:
            backtrack(target, op(cur,nums[i]), i+1, nums)

for line in tqdm(lines):
    target,nums = line.split(':')
    target = int(target)
    nums = [int(x) for x in nums.split()]
    backtrack(target,0,0,nums)

print(sum(totals))