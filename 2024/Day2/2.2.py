import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [[int(num) for num in x.split()] for x in data.split('\n')]

safe = 0
for line in lines:
    is_unsafe = False
    dir = -1 if line[0] > line[-1] else 1
    for i in range(1,len(line)):
        if line[i] < line[i-1] and dir == 1:
            is_unsafe = True
            break
        if line[i] > line[i-1] and dir == -1:
            is_unsafe = True
            break
        diff = abs(line[i] - line[i-1])
        if 1 > diff or  3 < diff:
            is_unsafe = True
            break
    if not is_unsafe:
        safe += 1
    else:
        combs = [line[:i] + line[i+1:] for i in range(len(line))]
        for comb in combs:
            is_unsafe = False
            dir = -1 if comb[0] > comb[-1] else 1
            for j in range(1,len(comb)):
                if comb[j] < comb[j-1] and dir == 1:
                    is_unsafe = True
                    break
                if comb[j] > comb[j-1] and dir == -1:
                    is_unsafe = True
                    break
                diff = abs(comb[j] - comb[j-1])
                if 1 > diff or  3 < diff:
                    is_unsafe = True
                    break
            if not is_unsafe:
                safe += 1
                break
print(safe)