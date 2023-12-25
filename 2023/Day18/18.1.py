import sys
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
dig_plan = [(row.split()[0], int(row.split()[1]), row.split()[2]) for row in data.split('\n')]

def calc_area(vertices):
  n = len(vertices)
  sum1 = 0
  sum2 = 0
  
  for i in range(n-1):
    sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
    sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  
  sum1 = sum1 + vertices[n-1][0]*vertices[0][1]   
  sum2 = sum2 + vertices[0][0]*vertices[n-1][1]   
  
  area = abs(sum1 - sum2) / 2
  return area

dirs = {'R': (0,1), 'L': (0,-1), 'U' : (-1,0), 'D' : (1,0)}
vertices = []
cur = [0,0]

for dir,steps,_ in dig_plan:
    for step in range(steps):
        cur[0] +=  dirs[dir][0] 
        cur[1] +=  dirs[dir][1]
        vertices.append(tuple(cur))


print(int(calc_area(vertices)) + (len(vertices) // 2) + 1)