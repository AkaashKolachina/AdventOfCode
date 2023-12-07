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
    for i in range(0,len(lines),3):
        sack_1 = lines[i]
        sack_2 = set(lines[i + 1])
        sack_3 = set(lines[i + 2])
        for letter in sack_1:
            if letter in sack_2 and letter in sack_3:
                total += priority[letter]
                break
    print(total)