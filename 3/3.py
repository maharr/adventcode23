import re

with open("3/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

symbols = set()
stars = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if not char.isnumeric() and not char == ".":
            symbols.add((x,y))
            if char == "*":
                stars[(x,y)]=[]

total = 0
number = 0
adjacent = False

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char.isnumeric():
            number = (number*10) + int(char)
            if not adjacent:
                for dx in range(-1,2,1):
                    for dy in range(-1,2,1):
                        if (x + dx,y + dy) in symbols:
                            adjacent = True         
            
        elif number != 0:
            if adjacent:
                total += number
            number = 0
            adjacent = False

print("Part 1",total)


number = 0

for r, row in enumerate(data):
    for n in re.finditer(r'\d+', row):
        around = {(c,r) for r in (r-1,r,r+1)
                        for c in range(n.start()-1,n.end()+1)}
        
        for a in around & stars.keys():
            stars[a].append(int(n.group()))

total = 0

for star in stars.values():

    if len(star) == 2:
        total += star[0] * star[1]

print("Part 2",total)











