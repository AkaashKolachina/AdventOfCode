import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

max_vals = {"red" : 12, "green" : 13, "blue" : 14}
sum_of_valid = 0
for line in lines:
    game_id, match_data = line.split(':')
    game_id = int(game_id.strip().split(' ')[-1])
    matches = match_data.strip().split(';')
    is_valid = True
    for match in matches:
        num_cubes = re.compile(r'(\d+) (\w+)').findall(match)
        for count,color in num_cubes:
            if int(count) > max_vals[color]:
                is_valid = False
                break

    if is_valid:
        sum_of_valid += game_id
print(sum_of_valid)