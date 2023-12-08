import sys
import re
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

gear_map = defaultdict(list)
for i,line in enumerate(lines):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        is_part = False
        for r in range(max(i - 1, 0), min(i + 2, len(lines))):
            for c in range(max(match.start() - 1, 0), min(match.end() + 1, len(lines[0]))):
                if lines[r][c] == '*':
                    gear_map[(r,c)].append(int(match.group()))

gear_sum = 0
for gear in gear_map:
    if len(gear_map[gear]) == 2:
        gear_sum += (gear_map[gear][0] * gear_map[gear][1])
print(gear_sum)