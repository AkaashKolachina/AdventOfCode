import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]
x = []
y = []
for line in lines:
    number1, number2 = map(float, line.split()) 
    line_list = list(line)
    x.append(number1)
    y.append(number2)

score = 0
for num in x:
    cnt = y.count(num)
    score += (num * cnt)

print(int(score))