HALT = 99
ADD = 1
MULT = 2
IN = 3
OUT = 4
JNZ = 5
JZ = 6
LT = 7
EQ = 8

def run(program, input = None):
    i = 0
    while True:
        op = program[i]
        if op == HALT:
            break
        elif op == IN:
            to_write = program[i + 1]
            program[to_write] = input
            i += 2
        else:
            # Handle codes with multiple modes
            op = str(op).zfill(4)
            modes = op[:-2][::-1]
            op = int(op[-2:])
            p1 = program[i + 1] if int(modes[0]) else program[program[i + 1]]
            if op == OUT:
                print(p1)
                i += 2
            else:
                p2 = program[i + 2] if int(modes[1]) else program[program[i + 2]]
                if op == JNZ:
                    i = p2 if p1 != 0 else i + 3
                elif op == JZ:
                    i = p2 if p1 == 0 else i + 3
                elif op == ADD:
                    program[program[i+3]] = p1 + p2
                    i += 4
                elif op == MULT:
                    program[program[i+3]] = p1 * p2
                    i += 4
                elif op == LT:
                    program[program[i+3]] = 1 if p1 < p2 else 0
                    i += 4
                elif op == EQ:
                    program[program[i+3]] = 1 if p1 == p2 else 0
                    i += 4