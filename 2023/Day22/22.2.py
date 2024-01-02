import sys
from collections import defaultdict

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

blocks = []
id = 0
for line in lines:
    block = []
    x1,y1,z1,x2,y2,z2 = line.replace('~', ',').split(',')
    x1,y1,z1,x2,y2,z2 = int(x1.strip()),int(y1.strip()),int(z1.strip()),int(x2.strip()),int(y2.strip()),int(z2.strip())
    for x in range(x1,x2+1):
         for y in range(y1,y2+1):
              for z in range(z1,z2+1):
                   block.append([x,y,z])
    blocks.append(block)

blocks.sort(key = lambda x: x[0][2])

supports = defaultdict(set)
supported_by = defaultdict(set)
settled = set()
ids = {}
id = 0

for block in blocks:
     has_settled = False
     sb = set()
     while not has_settled:
          for i in range(len(block)):
               block[i][2] -= 1
               x,y,z = block[i]
               if z < 1:
                    has_settled = True
               elif (x,y,z) in settled:
                    has_settled = True
                    sb.add(ids[(x,y,z)])
                    supports[ids[(x,y,z)]].add(id)

     for (x,y,z) in block:
        ids[(x,y,z+1)] = id
        settled.add((x,y,z+1))

     supported_by[id] = sb
     id += 1


def get_total_falls(id, fell):
     if not supports[id]:
          return 0
     
     total_falls = 0
     for i in supports[id]:
          if all(id2 in fell for id2 in supported_by[i]):
               fell.add(i)
               total_falls += 1 + get_total_falls(i, fell)
     return total_falls
               

fall_sum = 0
for i in range(len(blocks)):
     fell = {i}
     fall_sum += get_total_falls(i,fell)
print(fall_sum)