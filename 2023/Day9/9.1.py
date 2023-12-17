import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
readings = [[int(num) for num in x.split()] for x in data.split('\n')]

def get_next(data):
    if all([x == 0 for x in data]):
        return 0
    
    diffs = []
    for i in range(1,len(data)):
        diffs.append(data[i] - data[i - 1])
    
    next_val = get_next(diffs)
    return next_val + data[-1]

next_val_sum = 0
for reading in readings:
    next_val_sum += get_next(reading)
print(next_val_sum)