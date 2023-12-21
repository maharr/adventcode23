import math, re

with open("6/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

length = [int(x) for x in re.findall(r'(\d+)',data[0])]
distance = [int(x) for x in re.findall(r'(\d+)',data[1])]

ways = []

for d,t in enumerate(length):

    a = 1
    b = -t
    c = distance[d]

    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)

    ways.append(math.ceil(sol2)-math.floor(sol1)-1)

print('Q1 {0}'.format(math.prod(ways)))

longlength = 0
longdistance = 0

for l in length:
    longlength = (longlength * (10 ** len(str(l)))) + l

for d in distance:
    longdistance = (longdistance * (10 ** len(str(d)))) + d

a = 1
b = -longlength
c = longdistance

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)



print('Q2 {0}'.format(math.ceil(sol2)-math.floor(sol1)-1))