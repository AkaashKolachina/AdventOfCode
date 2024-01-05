import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
modules = [int(x) for x in data.split('\n')]

def get_fuel(mass):
    if mass <= 0:
        return 0
    fuel = (mass // 3) - 2
    extra_fuel = get_fuel(fuel)
    extra_fuel = extra_fuel if extra_fuel > 0 else 0
    return fuel + extra_fuel

total_fuel = 0
for module in modules:
    total_fuel += get_fuel(module)

print(total_fuel)