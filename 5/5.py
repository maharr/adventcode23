import re, math

with open("5/input.txt", "r") as f:
    global data 
    data = f.read().splitlines()

seeds = []
conversions = [[] for i in range(7)]
counter = -1


for line in data:
    numbers = [int(x) for x in re.findall(r"(\d+)", line)]
    if len(numbers) > 1:
        if counter == -1:
            seeds = numbers
            counter += 1
        else:
            offset = numbers[0] - numbers[1]
            conversions[counter].append([numbers[1],numbers[1]+numbers[2]-1,offset])

    elif len(conversions[counter]) > 0:   
        counter += 1

seedrange = []

for i in range(math.floor(len(seeds)/2)):
    seedrange.append([seeds[i*2], seeds[i*2] + seeds[(i*2)+1]-1])



counter = 1
for s,seed in enumerate(seeds):
    for step in conversions:
        for line in step:
            if line[0] <= seed <= line[1]:
                seed += line[2]
                seeds[s] = seed
                break
    
print(min(seeds))


for step in conversions:
    s = 0
    while s < len(seedrange):
        for line in step:
            if seedrange[s][1] < line[0]:
                pass
            elif seedrange[s][0] > line[1]:
                pass
            elif seedrange[s][0] >= line[0] and seedrange[s][1] <= line[1]:
                seedrange[s][0] += line[2]
                seedrange[s][1] += line[2]                
                break
            elif seedrange[s][0] < line[0] and seedrange[s][1] > line[1]:
                seedrange.append([seedrange[s][0],line[0]-1])
                seedrange.append([line[1]+1,seedrange[s][1]])
                seedrange[s][0] = line[0] + line[2]
                seedrange[s][1] = line[1] + line[2]
                break
            elif seedrange[s][0] < line[0] and seedrange[s][1] <= line[1]:
                seedrange.append([seedrange[s][0],line[0]-1])
                seedrange[s][0] = line[0] + line[2]
                seedrange[s][1] += line[2]
                break
            elif seedrange[s][0] >= line[0] and seedrange[s][1] > line[1]:
                seedrange.append([line[1]+1,seedrange[s][1]])
                seedrange[s][0] += line[2]
                seedrange[s][1] = line[1] + line[2]
                break
        s += 1
        


mymin = min([min(r) for r in seedrange])
print(mymin)

#seeds
#seed-soil  - 1
#soil-fert  - 2
#fert-water - 3
#water-light- 4
#light-temp - 5
#temp-hum   - 6
#hum-loc    - 7