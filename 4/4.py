import re

with open("4/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

total = 0

num_cards = [1 for x in data]

for l,line in enumerate(data):
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

    winning_line = l + 1

    for w in win:
        if w in num:
            num_cards[winning_line] += num_cards[l]
            winning_line += 1




    

print("Q1:",total)

print("Q2:", sum(num_cards))   