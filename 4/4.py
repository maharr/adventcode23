import re

with open("4/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

total = 0

for line in data:
    c, w, n = re.split(r': | \|', line)
    c = re.findall(r'(\d+)', c)
    card = [int(x) for x in c]
    w = re.findall(r'(\d+)', w)
    win = [int(x) for x in w]
    n = re.findall(r'(\d+)', n)
    num = [int(x) for x in n]

    cardtotal = 0

    for w in win:
        if w in num:
            if cardtotal == 0:
                cardtotal = 1
            else:
                cardtotal *= 2
    total += cardtotal
    

print(total)
    