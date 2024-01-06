HALT = 99
ADD = 1
MULT = 2
IN = 3
OUT = 4
JNZ = 5
JZ = 6
LT = 7
EQ = 8

class IntCode:

    def __init__(self,program, input = []):
        self.program = program
        self.input = input
        self.i = 0
    
    def add_input(self, to_add):
        self.input.append(to_add)

    def run(self):
        program = self.program
        outputs = []
        while True:
            op = program[self.i]
            if op == HALT:
                return None
            elif op == IN:
                to_write = program[self.i + 1]
                program[to_write] = self.input[0]
                self.input = self.input[1:]
                self.i += 2
            else:
                # Handle codes with multiple modes
                op = str(op).zfill(4)
                modes = op[:-2][::-1]
                op = int(op[-2:])
                p1 = program[self.i + 1] if int(modes[0]) else program[program[self.i + 1]]
                if op == OUT:
                    self.i += 2
                    return p1
                else:
                    p2 = program[self.i + 2] if int(modes[1]) else program[program[self.i + 2]]
                    if op == JNZ:
                        self.i = p2 if p1 != 0 else self.i + 3
                    elif op == JZ:
                        self.i = p2 if p1 == 0 else self.i + 3
                    elif op == ADD:
                        program[program[self.i+3]] = p1 + p2
                        self.i += 4
                    elif op == MULT:
                        program[program[self.i+3]] = p1 * p2
                        self.i += 4
                    elif op == LT:
                        program[program[self.i+3]] = 1 if p1 < p2 else 0
                        self.i += 4
                    elif op == EQ:
                        program[program[self.i+3]] = 1 if p1 == p2 else 0
                        self.i += 4