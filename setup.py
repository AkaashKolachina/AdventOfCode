import os
import shutil
import re

# Create Year Folders 
years = ["2022", "2023"]
days = ["Day{}".format(i) for i in range(1,26)]

for year in years:
    os.makedirs(year)
    for day in days:
        os.makedirs(os.path.join(year, day))


# For 2022 move our files into new structure.
files = [file for file in os.listdir() if os.path.isfile(file)]
for file in files:
    if file.strip().split('.')[0].isnumeric():
        i = int(file.strip().split('.')[0])
        shutil.move(file, os.path.join("2022", "Day{}".format(i)))
    elif re.match(r"d(\d+)input\.txt", file.strip()):
        i = int(re.match(r"d(\d+)input\.txt", file.strip()).group(1))
        shutil.move(file, os.path.join("2022", "Day{}".format(i)))

# For 2023 Setup python and blank input files
year = "2023"
for day in days:
    dir = os.path.join(year, day)
    files = ["{}.1.py".format(day[-1]), "{}.2.py".format(day[-1]), "input.txt", "test.txt"]
    for file in files:
        open(os.path.join(dir, file), 'a').close() 
