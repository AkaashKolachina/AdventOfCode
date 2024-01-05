import sys
import os

# Create Year and Day Folders 
year = sys.argv[1]
days = ["Day{}".format(i) for i in range(1,26)]
os.makedirs(year)
for day in days:
    os.makedirs(os.path.join(year, day))


# Setup python and blank input files
for i in range(1,26):
    day = "Day{}".format(i)
    dir = os.path.join(year, day)
    files = ["{}.1.py".format(i), "{}.2.py".format(i), "test.txt"]
    for file in files:
        open(os.path.join(dir, file), 'a').close()

    # Add code to read in input for ever part 1 file 
    f = open(os.path.join(dir, "{}.1.py".format(i)), "a")
    f.write('import sys\n\n')
    f.write("input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'\n")
    f.write('data = open(input).read().strip()\n')
    f.write("lines = [x for x in data.split('\\n')]\n")
    f.close()