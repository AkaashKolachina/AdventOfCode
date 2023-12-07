from sys import argv

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
score = 1
priority = {}
for letter in alphabet:
    priority[letter] = score
    score += 1


with open(argv[1], "r") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        n = len(line) / 2
        sack_1 = line[:n]
        sack_2 = line[n:]
        sack_2 = set(sack_2)
        for letter in sack_1:
            if letter in sack_2:
                total += priority[letter]
                break
    print(total)