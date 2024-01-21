import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

ic = IntCode(program.copy(), [2])
outputs = ic.run_no_halt()
for output in outputs:
    print(output)