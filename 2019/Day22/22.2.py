import sys
from tqdm import tqdm

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')][::-1]

num_cards = 119315717514047
card = 2020
a = 1
b = 0
k = 101741582076661
for line in lines:
    words = line.split()
    if words[0] == 'cut':
        cut_val = int(words[-1])
        if cut_val < 0:
            cut_val += num_cards
        #card = card + cut_val % num_cards
        b += cut_val 
    else:
        if words[-1].isnumeric():
            deal_val = int(words[-1])
            #card = pow(deal_val,-1,num_cards) * card % num_cards
            step_a = pow(deal_val,-1,num_cards)
            a *= step_a
            b *= step_a
        else:
            #card = -card + num_cards - 1
            a *= -1
            b *= -1
            b += num_cards - 1

a_part = pow(a,k,num_cards)
numer = ((b % num_cards) * ((1 - pow(a,k,num_cards)) % num_cards)) % num_cards
denom = (1 - (a % num_cards)) % num_cards
b_part = (numer * pow(denom,-1,num_cards)) % num_cards
print((((a_part * card) % num_cards) + b_part) % num_cards)