import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [list(x) for x in data.split('\n')]

patterns = [[]]
for line in lines:
    if line == []:
        patterns.append([])
    else:
        patterns[-1].append(line)

def get_axis(pattern):
    for idx in range(len(pattern) - 1):
        i = idx
        j = i + 1
        if pattern[i] == pattern[j]:
            pos_axis = i
            is_reflection = True
            while i >= 0 and j < len(pattern):
                if pattern[i] != pattern[j]:
                    is_reflection = False
                    break
                i -= 1
                j += 1
            if is_reflection:
                return pos_axis + 1
    return -1

num_verts = 0
num_horiz = 0
for pattern in patterns:
    pattern_t = list(map(list, zip(*pattern)))
    vert_axis = get_axis(pattern_t)
    if vert_axis != -1:
        num_verts += vert_axis
    else:
        num_horiz += get_axis(pattern)
print(num_verts + 100*num_horiz)