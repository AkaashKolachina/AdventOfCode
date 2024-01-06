import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()

phase_settings = [i for i in range(5)]

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
    for i in range(5):
        program = [int(x) for x in data.split(',')]
        ic = IntCode(program,[perm[i], input_signal])
        output = ic.run()
        while output is not None:
            input_signal = output
            output = ic.run()
    max_output = max(max_output,input_signal)
print(max_output)