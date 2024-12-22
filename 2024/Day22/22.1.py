import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [int(x) for x in data.split('\n')]

mod_num = 16777216

def get_next_secret(num):
    secret = (num ^ (num*64)) % mod_num
    result = secret // 32
    secret ^= result
    secret %= mod_num
    result = secret * 2048
    secret ^= result
    secret %= mod_num
    return secret

secret_sum = 0
for num in lines:
    secret = num
    for _ in range(2000):
        secret = get_next_secret(secret)
    secret_sum += secret
print(secret_sum)
    