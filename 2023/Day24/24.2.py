import sys
from z3 import *

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

point_data = []
for line in lines:
    point_data.append([])
    for data in line.split('@'):
        vector = []
        for num in data.strip().split(','):
            vector.append(int(num))
        point_data[-1].append(tuple(vector))
    point_data[-1] = tuple(point_data[-1])

s = Solver()
x = Real('x')
y = Real('y')
z = Real('z')
vx = Real('vx')
vy = Real('vy')
vz = Real('vz')

for i in range(len(point_data)):
    (x_i,y_i,z_i), (vx_i,vy_i,vz_i) = point_data[i]
    t = Real(f't_{i}')
    s.add(x + t*vx - x_i - t*vx_i == 0)
    s.add(y + t*vy - y_i - t*vy_i == 0)
    s.add(z + t*vz - z_i - t*vz_i == 0)

s.check()
print(s.model().eval(x+y+z))