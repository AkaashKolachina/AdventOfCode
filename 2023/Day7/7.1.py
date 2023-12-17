import sys
from collections import Counter
import functools

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

hand_to_val = {"T":10, "J":11,"Q":12,"K":13,"A":14}

def get_hand_type(hand):
    hand_freqs = Counter(hand).values()
    if 5 in hand_freqs:
        return 7 # 5 of a kind
    elif 4 in hand_freqs:
        return 6 # 4 of a kind
    elif 3 in hand_freqs:
        if 2 in hand_freqs:
            return 5 # Full House
        else:
            return 4 # 3 of a kind
    elif 2 in hand_freqs:
        if Counter(hand_freqs)[2] > 1:
            return 3 # Two Pair
        else:
            return 2 # Two of a Kind
    else:
        return 1 # High Card

def compare(hd_1, hd_2):
    hand_1,_ = hd_1
    hand_2,_ = hd_2
    hand_1_type = get_hand_type(hand_1)
    hand_2_type = get_hand_type(hand_2)

    if hand_1_type > hand_2_type:
        return 1
    elif hand_1_type < hand_2_type:
        return -1
    else:
        for i in range(len(hand_1)):
            if hand_1[i] != hand_2[i]:
                return 1 if hand_1[i] > hand_2[i] else -1
        return 0 # Only if exact same hand

hand_data = []
for line in lines:
    hand,bid = line.split(' ')
    hand = [int(hand[i]) if hand[i].isnumeric() else hand_to_val[hand[i]] for i in range(len(hand))]
    hand_data.append((hand,int(bid)))


hand_data = sorted(hand_data, key=functools.cmp_to_key(compare))

winnings = 0
rank = 1
for hand,bid in hand_data:
    winnings += (bid * rank)
    rank += 1
print(winnings)