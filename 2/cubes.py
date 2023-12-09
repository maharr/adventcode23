import re

with open("2/input.txt", "r") as f:
    global data 
    data = f.readlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

gameids = 0

for game,line in enumerate(data):
    possible = True
    for count, colour in re.findall(r'(\d+) (\w+)', line):
        if int(count) > bag[colour]:
            possible = False
    if possible:
        gameids += game + 1 

print("Sum of game IDs",gameids)

powers = 0

for line in data:
    minimum = {"red":0, "green":0, "blue": 0}
    for count, colour in re.findall(r'(\d+) (\w+)', line):
        minimum[colour] = max(int(count),minimum[colour])
    product = 1

    for val in minimum.values():
        product *= val
    
    powers += product

print("Sum of powers", powers)








