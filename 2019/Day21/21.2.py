import sys
sys.path.append('..')
from intcode import IntCode

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
program = [int(x) for x in data.split(',')]

inputs = ['NOT A J',
          'NOT B T',
          'OR T J',
          'NOT C T',
          'OR T J',
          'AND D J',
          'NOT E T',
          'NOT T T',
          'OR H T',
          'AND T J',
          'RUN',
          '']
input = '\n'.join(inputs)
input = [ord(char) for char in input]
ic = IntCode(program,input)
outputs = []
has_halted = False
while not has_halted:
    output = ic.run()
    if output is None:
        has_halted = True
    else:
        if output <= 255:
            outputs.append(chr(output))
        else:
            outputs.append(str(output))


print(''.join(outputs))