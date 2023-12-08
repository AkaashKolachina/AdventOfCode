import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

sum_of_powers = 0
for line in lines:
    game_id, match_data = line.split(':')
    game_id = int(game_id.strip().split(' ')[-1])
    matches = match_data.strip().split(';')
    min_needed = {"red" : 0, "green" : 0, "blue" : 0}

    for match in matches:
        num_cubes = re.compile(r'(\d+) (\w+)').findall(match)
        for count,color in num_cubes:
            min_needed[color] = max(min_needed[color], int(count))
    power = 1
    for color in min_needed:
        power *= min_needed[color]
    sum_of_powers += power

print(sum_of_powers)