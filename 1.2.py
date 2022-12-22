from sys import argv

with open(argv[1], "r") as f:
    lines = f.readlines()
    mx = [0,0,0]
    cur_max = 0
    for line in lines:
        if line.strip():
            cur_max += int(line)
        else:
            i = mx.index(min(mx))
            mx[i] = max(cur_max,mx[i])
            cur_max = 0
    print(sum(mx))