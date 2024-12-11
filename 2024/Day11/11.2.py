import sys
from collections import Counter

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
stones = list(map(int, data.split()))
stone_cnt = Counter(stones)

def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        num1 = int(str_stone[:len(str_stone) // 2])
        num2 = int(str_stone[len(str_stone) // 2:])
        return [num1,num2]
    else:
        return [2024*stone]


for _ in range(75):
    stone_cnt_after_blink = Counter()
    for stone in stone_cnt:
        for next_stone in blink(stone):
            stone_cnt_after_blink[next_stone] += stone_cnt[stone]
    stone_cnt = stone_cnt_after_blink

print(sum(stone_cnt.values()))