import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
image = open(input).read().strip()

num_rows = 6
num_cols = 25
step = num_rows * num_cols
layer_data = [(image[i:i+step].count('0'),image[i:i+step].count('1') * image[i:i+step].count('2')) for i in range(0,len(image), step)]
print(min(layer_data)[1])