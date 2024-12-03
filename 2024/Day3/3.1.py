import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()

matches = re.findall(r"mul\((-?\d+),\s*(-?\d+)\)", data)

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])
print(total)
