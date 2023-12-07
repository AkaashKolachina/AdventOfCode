from sys import argv

num_pairs = 0

with open(argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        ranges = line.split(',')
        elf_1 = ranges[0].split('-')
        elf_2 = ranges[1].split('-')
        
        if (int(elf_1[0]) <= int(elf_2[0]) and int(elf_2[0]) <= int(elf_1[1])) or  (int(elf_1[0]) <= int(elf_2[1]) and int(elf_2[1]) <= int(elf_1[1])):
            num_pairs += 1
        elif (int(elf_2[0]) <= int(elf_1[0]) and int(elf_1[0]) <= int(elf_2[1])) or  (int(elf_2[0]) <= int(elf_1[1]) and int(elf_1[1]) <= int(elf_2[1])):
            num_pairs += 1
    print(num_pairs)