from sys import argv

d = {}
with open(argv[1], "r") as f:
    lines = f.readlines()
    line = lines[0]
    for i in range(13):
        d[line[i]] = d.get(line[i],0) + 1
    #print(d)
    for i in range(13, len(line)):
        
        d[line[i]] = d.get(line[i],0) + 1
        good = True
        for key in d:
            if d[key] > 1:
                good = False
                break
        if good:
            print(i+1)
            break
        else:      
            d[line[i - 13]] = d.get(line[i - 13],0) - 1