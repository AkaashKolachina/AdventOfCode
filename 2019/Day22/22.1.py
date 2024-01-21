import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

num_cards = 10007
cards = [i for i in range(num_cards)]

for line in lines:
    words = line.split()
    if words[0] == 'cut':
        cut_val = int(words[-1])
        cards = cards[cut_val:] + cards[:cut_val]
    else:
        if words[-1].isnumeric():
            deal_val = int(words[-1])
            shuffled = [0 for _ in range(num_cards)]
            for i,card in enumerate(cards):
                shuffled[(i*deal_val) % num_cards] = card
            cards = shuffled
        else:
            cards = cards[::-1]

print(cards.index(2019))