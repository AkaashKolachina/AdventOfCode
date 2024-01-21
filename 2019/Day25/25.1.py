import sys
sys.path.append('..')
from intcode import IntCode
from itertools import chain, combinations

file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(file).read().strip()
program = [int(x) for x in data.split(',')]
ic = IntCode(program)

def send_input(ic_input):
    for char in ic_input:
        ic.add_input(ord(char))
    ic.add_input(10)

outputs = []
#history = []
commands = ['west', 'take semiconductor', 'west', 'take planetoid', 'west', 'take food ration', 'west', 'take fixed point', 'west', 'take klein bottle', 'east', 'south', 'west', 'take weather machine', 'east', 'north', 'east', 'south', 'north', 'east', 'south', 'south', 'south', 'take pointer', 'north', 'north', 'east', 'take coin', 'east', 'south', 'north', 'north', 'east', 'inv']
items = ['food ration', 'fixed point', 'weather machine', 'semiconductor', 'planetoid', 'coin', 'pointer', 'klein bottle']
DROP = 'drop {}'
TAKE = 'take {}'
def drop_items(items):
    return [DROP.format(item) for item in items]
def take_items(items):
    return [TAKE.format(item) for item in items]

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
commands += drop_items(items)
subsets = powerset(items)
for subset in subsets:
    commands += take_items(subset)
    commands.append('north')
    commands += drop_items(subset)

while True:
    output = ic.run()
    if output is not None:
        outputs.append(output)
    else:
        print(''.join([chr(out) for out in outputs]))
        outputs = []
        if not ic.has_halted:
            #user_input = input('> ')
            user_input = commands.pop(0)
            #if user_input == 'exit':
            #    break
            #history.append(user_input)
            send_input(user_input)
        else:
            break
#print(history)
