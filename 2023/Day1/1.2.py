import sys
import re

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

num_map = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
keys = list(num_map.keys())
for key in keys:
    num_map[key[::-1]] = num_map[key]

def get_num(line, re_cond):
    first_num = re.search(r'\d', line)
    first_word = re.search(re_cond, line, re.IGNORECASE)
    first = -1
    if first_num and first_word:
        first = int(first_num.group()) if first_num.start() < first_word.start() else num_map[first_word.group()]
    elif first_num:
        first = int(first_num.group())
    else:
        first = num_map[first_word.group()]
    return first

total = 0
for line in lines:
    re_str1 = r'(one|two|three|four|five|six|seven|eight|nine)'
    re_str2 = r'enin|thgie|neves|xis|evif|ruof|eerht|owt|eno'
    first = get_num(line, re_str1)
    last = get_num(line[::-1], re_str2)
    num = first*10 + last
    #print(num)
    total += num

print(total)