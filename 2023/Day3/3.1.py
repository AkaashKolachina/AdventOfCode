import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

part_sum = 0
for i,line in enumerate(lines):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        is_part = False
        for r in range(max(i - 1, 0), min(i + 2, len(lines))):
            for c in range(max(match.start() - 1, 0), min(match.end() + 1, len(lines[0]))):
                if not lines[r][c].isnumeric() and lines[r][c] != '.':
                    is_part = True
                    break
            if is_part:
                break
        if is_part:
            part_sum += int(match.group())
print(part_sum)