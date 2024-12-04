import sys

input = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(input).read().strip()
grid = [list(x) for x in data.split('\n')]

TARGET = 'XMAS'
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == TARGET[0]:
            if i + len(TARGET) <= len(grid):
               if all(grid[i + k][j] == TARGET[k] for k in range(len(TARGET))):
                    count += 1
            if 0 <= i - len(TARGET) + 1:
                if all(grid[i - k][j] == TARGET[k] for k in range(len(TARGET))):
                    count += 1  
            if j + len(TARGET) <= len(grid[0]):
               if all(grid[i][j + k] == TARGET[k] for k in range(len(TARGET))):
                    count += 1
            if 0 <= j - len(TARGET) + 1:
                if all(grid[i][j - k] == TARGET[k] for k in range(len(TARGET))):
                    count += 1
            if i + len(TARGET) <= len(grid) and j + len(TARGET) <= len(grid[0]):
               if all(grid[i + k][j + k] == TARGET[k] for k in range(len(TARGET))):
                    count += 1    
            if 0 <= i - len(TARGET) + 1 and j + len(TARGET) <= len(grid[0]):
               if all(grid[i - k][j + k] == TARGET[k] for k in range(len(TARGET))):
                    count += 1
            if i + len(TARGET) <= len(grid) and 0 <= j - len(TARGET) + 1:
               if all(grid[i + k][j - k] == TARGET[k] for k in range(len(TARGET))):
                    count += 1   
            if 0 <= i - len(TARGET) + 1 < len(grid) and 0 <= j - len(TARGET) + 1:
               if all(grid[i - k][j - k] == TARGET[k] for k in range(len(TARGET))):
                    count += 1                 
print(count)
