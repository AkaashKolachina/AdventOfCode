import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
image = open(input).read().strip()

num_rows = 6
num_cols = 25
step = num_rows * num_cols
final_image = [[0 for j in range(num_cols)] for i in range(num_rows)]

for r in range(num_rows):
    for c in range(num_cols):
        for i in range(r * num_cols + c, len(image), step):
            # Space for black, hashtag for white
            if image[i] == '0':
                final_image[r][c] = ' '
                break
            elif image[i] == '1':
                final_image[r][c] = '#'
                break

for line in final_image:
    print(''.join(line))