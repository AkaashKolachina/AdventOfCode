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
x.sort()
y.sort()
pairs = zip(x,y)
sum = 0
for pair in pairs:
    sum += abs(pair[0] - pair[1])
print(int(sum))