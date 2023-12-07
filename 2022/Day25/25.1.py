from sys import argv

data = open(argv[1]).read().strip().split('\n')
lines = [x for x in data]

convert = {'-': -1, '=' :-2}

sum = 0
for line in lines:
    num = 0
    for i in range(len(line)):
        place = len(line) - i - 1
        digit = line[i]
        if digit.isnumeric():
            digit = int(digit)
        else:
            digit = convert[digit]
        num += digit * 5**place
    sum += num
print(sum)

dividend = sum
snafu = ''
while dividend:
    quotient = dividend // 5
    rem = dividend % 5
    if rem == 3:
        rem = '='
        quotient += 1
    elif rem == 4:
        rem = '-'
        quotient += 1
    else:
         rem = str(rem)

    snafu += rem
    dividend = quotient

print(snafu[::-1])
