import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

HALT = 99
ADD = 1
MULT = 2

def run(program):
    for pos in range(0,len(program),4):
        if program[pos] == HALT:
            break
        elif program[pos] == ADD:
            i = program[pos + 1]
            j = program[pos + 2]
            out = program[pos + 3]
            program[out] = program[i] + program[j]
        elif program[pos] == MULT:
            i = program[pos + 1]
            j = program[pos + 2]
            out = program[pos + 3]
            program[out] = program[i] * program[j]

target = 19690720
for noun in range(100):
    for verb in range(100):
        program = [int(x) for x in data.split(',')]
        program[1] = noun
        program[2] = verb
        run(program)
        if program[0] == target:
            print(100*noun + verb)
            exit()