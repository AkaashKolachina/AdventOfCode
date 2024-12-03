import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()

pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
matches = [(match.start(),match.group()) for match in re.finditer(pattern, data)]

donts = [(dont_match.start(), dont_match.group()) for dont_match in re.finditer(r"don't\(\)", data)]
dos = [(do_match.start(), do_match.group()) for do_match in re.finditer(r"do\(\)", data)]

memory = donts + matches + dos
memory.sort()

total = 0
can_add = True
for _,code in memory:
    if code == "don't()":
        can_add = False
    elif code == "do()":
        can_add = True
    else:
        if can_add:
            match = re.findall(r"mul\((-?\d+),\s*(-?\d+)\)", code)[0]
            total += (int(match[0]) * int(match[1]))
print(total)