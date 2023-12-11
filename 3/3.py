with open("3/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

symbols = set()

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if not char.isnumeric() and not char == ".":
            for dx in range(-1,2,1):
                for dy in range(-1,2,1):
                    symbols.add((x + dx, y + dy))

total = 0
number = 0
adjacent = False

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char.isnumeric():
            number = (number*10) + int(char)
            if (x,y) in symbols:
                adjacent = True
        elif number != 0:
            if adjacent:
                total += number
            number = 0
            adjacent = False

print(total)




