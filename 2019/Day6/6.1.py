import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

orbits = {}
for line in lines:
    ob1,ob2 = line.split(')')
    orbits[ob2] = ob1

def total_orbits(object):
    if object not in orbits:
        return 0
    return 1 + total_orbits(orbits[object])

check_sum = 0
for object in orbits:
    check_sum += total_orbits(object)
print(check_sum)