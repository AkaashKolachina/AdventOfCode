from sys import argv
from collections import deque

key = 811589153
data = open(argv[1]).read().strip().split('\n')
dict = [int(x) * key for x in data]
n = len(dict)
file = [num for num in range(n)]

for _ in range(10):
    for i in range(n):
        dist = dict[i]
        idx = file.index(i)
        file.remove(i)
        new_idx = (idx + dist) % len(file)
        file.insert(new_idx,i)
    
for i in range(n):
    file[i] = dict[file[i]]

i = file.index(0)
coords = (file[(i + 1000) % n],file[(i + 2000) % n],file[(i + 3000) % n])
print(coords)
print(sum(coords))

