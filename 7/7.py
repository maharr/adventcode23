from collections import Counter

with open("7/test.txt", "r") as f:
    global data 
    data = f.read().splitlines()

cardvalues = {
    "A":12,
    "K":11,
    "Q":10,
    "J":9,
    "T":8,
    "9":7,
    "8":6,
    "7":5,
    "6":4,
    "5":3,
    "4":2,
    "3":1,
    "2":0
}

hands = {}

for line in data:
    hands[(line[:5],int(line[6:]))] = 0

print(hands)
for l,line in enumerate(hands):
    handweight = 0
    for c,card in enumerate(line[0]):
        handweight += cardvalues[card] * (13**(4-c))

    c = Counter(line[0])
    if c.most_common()[0][1] == 5:
        handweight += 6 * (13**(5))
        print("Five of a kind")
    elif c.most_common()[0][1] == 4:
        handweight += 5 * (13**(5))
        print("Four of a kind")
    elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
        handweight += 4 * (13**(5))
        print("Full house")
    elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 1:
        handweight += 3 * (13**(5))
        print("Three of a kind")
    elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
        handweight += 2 * (13**(5))
        print("Two pair")
    elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 1:
        handweight += 1 * (13**(5))
        print("One pair")
    else:
        handweight += 0 * (13**(5))
        print("High card")

    hands[line] = handweight

rank = 1
total = 0
for hand in sorted(hands.items(),key=lambda item: item[1]):
    total += rank * hand[0][1]
    rank += 1

print(total)

print(hands)
for l,line in enumerate(hands):
    handweight = 0
    for c,card in enumerate(line[0]):
        handweight += cardvalues[card] * (13**(4-c))

    c = Counter(line[0])
    j = c["J"]
    if c.most_common()[0][1] + j == 5:
        handweight += 6 * (13**(5))
        print("Five of a kind")
    elif c.most_common()[0][1] + j  == 4:
        handweight += 5 * (13**(5))
        print("Four of a kind")
    elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
        handweight += 4 * (13**(5))
        print("Full house")
    elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 1:
        handweight += 3 * (13**(5))
        print("Three of a kind")
    elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
        handweight += 2 * (13**(5))
        print("Two pair")
    elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 1:
        handweight += 1 * (13**(5))
        print("One pair")
    else:
        handweight += 0 * (13**(5))
        print("High card")

    hands[line] = handweight

rank = 1
total = 0
for hand in sorted(hands.items(),key=lambda item: item[1]):
    total += rank * hand[0][1]
    rank += 1
