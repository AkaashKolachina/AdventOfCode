import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
lines = [x for x in data.split('\n')]

reg = []
for line in lines[:3]:
    reg.append(int(line.split(':')[1].strip()))

program = list(lines[-1].split(':')[1].split(','))
program = [int(x) for x in program]

def get_combo_val(operand):
    if 0 <= operand <= 3:
        return operand
    else:
        return reg[operand - 4]

# ip = 0
# out = []
# while ip < len(program) - 1:
#     opcode = program[ip]
#     operand = program[ip + 1]
#     has_jumped = False
#     if opcode == 0:
#         #adv
#         print("A = A({}) / 2 ** {} ({}), {}, operand:{}".format(reg[0],get_combo_val(operand), int(2**get_combo_val(operand)), reg[0] // (2**get_combo_val(operand)), operand))
#         reg[0] = reg[0] // (2**get_combo_val(operand))
#     elif opcode == 1:
#         #bxl
#         print("B = B({}) ^ {}, {}".format(reg[1], operand,reg[1] ^ operand))
#         reg[1] = (reg[1] ^ operand)
#     elif opcode == 2:
#         #bst
#         print("B = {} % 8, {}".format(get_combo_val(operand), get_combo_val(operand) % 8))
#         reg[1] = get_combo_val(operand) % 8
#     elif opcode == 3:
#         #jnx
#         if reg[0] == 0:
#             print("A is 0 - No Jump")
#         if reg[0] != 0:
#             print('A is {}, jump to {}'.format(reg[0], operand))
#             ip = operand
#             has_jumped = True
#     elif opcode == 4:
#         #bxc
#         print("B = B({}) ^ C({}), {}".format(reg[1], reg[2], reg[1] ^ reg[2]))
#         reg[1] = reg[1] ^ reg[2]
#     elif opcode == 5:
#         #out
#         print("Output: {} % 8, {}".format(get_combo_val(operand), get_combo_val(operand) % 8))
#         out.append(str(get_combo_val(operand) % 8))
#     elif opcode == 6:
#         #bdv
#         print("B = A({}) / 2 ** {} ({}), {}, operand:{}".format(reg[0],get_combo_val(operand), int(2**get_combo_val(operand)), reg[0] // (2**get_combo_val(operand)), operand))
#         reg[1] = reg[0] // (2**get_combo_val(operand))
#     else:
#         #cdv
#         print("C = A({}) / 2 ** {} ({}), {}, operand:{}".format(reg[0],get_combo_val(operand), int(2**get_combo_val(operand)), reg[0] // (2**get_combo_val(operand)), operand))
#         reg[2] = reg[0] // (2**get_combo_val(operand))
#     if not has_jumped:
#         ip += 2
# A = 41644071
# while A != 0:
#     B = A % 8
#     B = B ^ 2
#     C = A // (2**B)
#     B = B ^ 7
#     B = B ^ C
#     A = A // 8
#     print(B % 8)

def next_out(A):
    B = A % 8
    B = B ^ 2
    C = A // (2**B)
    B = B ^ 7
    B = B ^ C
    A = A // 8
    return B % 8

possible_As = []
def backtrack(A, i):
    if next_out(A) != program[i]:
        return
    elif i == 0:
        possible_As.append(A)
    else:
        for inc in range(8):
            backtrack(A*8  + inc, i - 1)

for inc in range(8):
    backtrack(inc,len(program) - 1)
print(min(possible_As))