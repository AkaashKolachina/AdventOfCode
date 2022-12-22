from sys import argv
from collections import defaultdict

PATH = ''
dir_sizes = defaultdict(int)

def handle_cd(PATH, arg):
    if arg == '/':
        return '/'
    elif arg == '..':
        idx = len(PATH) - PATH[::-1].index('/') - 1
        return PATH[:idx]
    else:
        PATH += '/' + arg
        return PATH

def update_size(PATH, size,ds):
    path = PATH
    while path != '':
        ds[path] += size
        idx = len(path) - path[::-1].index('/') - 1
        path = path[:idx]

with open(argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        inputs = line.split(' ')
        if inputs[0].strip() == '$' and inputs[1].strip() == 'cd':
            PATH = handle_cd(PATH,inputs[2].strip())
        elif inputs[0].strip().isnumeric():
            size = int(inputs[0].strip())
            update_size(PATH, size,dir_sizes)
    
    vals = dir_sizes.values()
    sum = 0
    for val in vals:
        if val <= 100000:
            sum += val
    print(sum)