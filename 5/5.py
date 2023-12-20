import re

with open("5/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

conversions = [[] for i in range(8)]
counter = 0


for line in data:
    numbers = [int(x) for x in re.findall(r"(\d+)", line)]
    if len(numbers) > 1:
        if counter == 0:
            conversions[counter] = numbers
        else:
            offset = numbers[0] - numbers[1]
            conversions[counter].append([numbers[1],numbers[1]+numbers[2]-1,offset])

    elif len(conversions[counter]) > 0:   
        counter += 1

counter = 1
for s,seed in enumerate(conversions[0]):
    for step in conversions[1:]:
        for line in step:
            if line[0] <= seed <= line[1]:
                seed = seed + line[2]
                conversions[0][s] = seed
                break
    
print(min(conversions[0]))

#seeds
#seed-soil  - 1
#soil-fert  - 2
#fert-water - 3
#water-light- 4
#light-temp - 5
#temp-hum   - 6
#hum-loc    - 7