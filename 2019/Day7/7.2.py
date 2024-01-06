import sys
sys.path.append('..')
from intcode import IntCode
from collections import deque

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

phase_settings = [i for i in range(5,10)]
permutations = []
def find_permutations(cur_perm, options):
    if not options:
        permutations.append(cur_perm)
        return
    for i,option in enumerate(options):
        find_permutations(cur_perm + [option], options[:i] + options[i+1:])

find_permutations([], phase_settings)


max_output = 0
for perm in permutations:
    input_signal = 0
    amps = [IntCode(program.copy(),[perm[i]]) for i in range(5)]
    outputs = [0 for _ in range(5)]
    i = 0
    while True:
        amps[i].add_input(input_signal)
        output = amps[i].run()
        if output is not None:
            input_signal = output
            outputs[i] = input_signal
        else:
            max_output = max(max_output,outputs[-1])
            break
        i = (i+1) % len(amps)
print(max_output)