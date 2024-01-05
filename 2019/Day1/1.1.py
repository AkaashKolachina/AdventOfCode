import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
modules = [int(x) for x in data.split('\n')]

total_fuel = 0
for module in modules:
    total_fuel += (module // 3) - 2

print(total_fuel)