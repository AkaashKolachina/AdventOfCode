import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()

is_free = False
disk = []
id = -1
for num in data:
    if not is_free:
        id += 1
    cnt = int(num)
    char = '.' if is_free else id
    char = str(char)
    for _ in range(cnt):
        disk.append(char)
    is_free = not is_free

left = 0
right = len(disk) - 1
while True:
    while disk[left] != '.':
        left += 1
    while disk[right] == '.':
        right -= 1
    if left < right:
        disk[left] = disk[right]
        disk[right] = '.'
    else:
        break

checksum = 0
idx = 0
while disk[idx] != '.':
    checksum += idx * int(disk[idx])
    idx += 1
print(checksum)