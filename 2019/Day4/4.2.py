import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
start,end = data.split('-')
start,end = int(start), int(end)

def is_valid(num):
    groups = []
    count = 1
    for i in range(1,len(num)):
        if int(num[i]) < int(num[i-1]):
            return False
        if num[i] == num[i-1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)
    return 2 in groups

num_possible = 0
for num in range(start, end + 1):
    num_possible += 1 if is_valid(str(num)) else 0
print(num_possible)