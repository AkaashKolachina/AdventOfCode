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

ip = 0
out = []
while ip < len(program) - 1:
    opcode = program[ip]
    operand = program[ip + 1]
    has_jumped = False
    if opcode == 0:
        #adv
        reg[0] = reg[0] // (2**get_combo_val(operand))
    elif opcode == 1:
        #bxl
        reg[1] = (reg[1] ^ operand)
    elif opcode == 2:
        #bst
        reg[1] = get_combo_val(operand) % 8
    elif opcode == 3:
        #jnx
        if reg[0] != 0:
            ip = operand
            has_jumped = True
    elif opcode == 4:
        #bxc
        reg[1] = reg[1] ^ reg[2]
    elif opcode == 5:
        #out
        out.append(str(get_combo_val(operand) % 8))
    elif opcode == 6:
        #bdv
        reg[1] = reg[0] // (2**get_combo_val(operand))
    else:
        #cdv
        reg[2] = reg[0] // (2**get_combo_val(operand))
    if not has_jumped:
        ip += 2

print(','.join(out))