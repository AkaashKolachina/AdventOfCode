import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
stones = list(map(int, data.split()))

def blink():
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            str_stone = str(stones[i])
            num1 = int(str_stone[:len(str_stone) // 2])
            num2 = int(str_stone[len(str_stone) // 2:])
            stones[i] = num1
            stones.insert(i+1,num2)
            i += 1
        else:
            stones[i] *= 2024
        i += 1

for _ in range(25):
    blink()

print(len(stones))