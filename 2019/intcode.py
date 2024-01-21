from collections import defaultdict

# Opcodes
HALT = 99
ADD = 1
MULT = 2
IN = 3
OUT = 4
JNZ = 5
JZ = 6
LT = 7
EQ = 8
RBO = 9

# Modes
POS = 0
IMM = 1
REL = 2

class IntCode:

    def __init__(self, program, input = []):
        self.program = defaultdict(int)
        for i,val in enumerate(program):
            self.program[i] = val

        self.input = input
        self.i = 0
        self.rel_base = 0
        self.has_halted = False
    
    def add_input(self, to_add):
        self.input.append(to_add)
    
    def get_params(self, modes):
        p = []
        for i in range(2):
            if int(modes[i]) == POS:
                p.append(self.program[self.program[self.i + i + 1]])
            elif int(modes[i]) == IMM:
                p.append(self.program[self.i + i + 1])
            elif int(modes[i]) == REL:
                p.append(self.program[self.rel_base + self.program[self.i + i + 1]])
        return p

    def run(self):
        program = self.program
        while True:
            op = program[self.i]
            op = str(op).zfill(5)
            modes = op[:-2][::-1]
            op = int(op[-2:])
            p1,p2 = self.get_params(modes)
            p3 = None
            if int(modes[2]) == REL:
                p3 = program[self.i + 3] + self.rel_base
            else:
                p3 = program[self.i + 3]
            if op == IN:
                if not self.input:
                    return None
                to_write = None
                if int(modes[0]) == REL:
                    to_write = program[self.i + 1] + self.rel_base
                else:
                    to_write = program[self.i + 1]
                program[to_write] = self.input[0]
                self.input = self.input[1:]
                self.i += 2 
            elif op == OUT:
                self.i += 2
                return p1
            elif op == RBO:
                self.rel_base += p1
                self.i += 2
            elif op == JNZ:
                self.i = p2 if p1 != 0 else self.i + 3
            elif op == JZ:
                self.i = p2 if p1 == 0 else self.i + 3
            elif op == ADD:
                program[p3] = p1 + p2
                self.i += 4
            elif op == MULT:
                program[p3] = p1 * p2
                self.i += 4
            elif op == LT:
                program[p3] = 1 if p1 < p2 else 0
                self.i += 4
            elif op == EQ:
                program[p3] = 1 if p1 == p2 else 0
                self.i += 4
            else:
                self.has_halted = True
                return None
            
    def run_no_halt(self):
        outputs = []
        has_halted = False
        while not has_halted:
            output = self.run()
            if output is not None:
                outputs.append(output)
            else:
                has_halted = True
        return outputs