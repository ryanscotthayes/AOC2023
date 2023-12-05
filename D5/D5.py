with open(r'./AOC2023/D5/D5.data') as f:
    lines = f.read().split('\n\n')

for i in lines:
    seeds = [int(v) for v in lines[0].split(': ')[1].split(' ')]
    seed2soil = [[int(v) for v in row] for row in [x.split(' ') for x in lines[1].split('\n')[1:]]]
    soil2fert = [[int(v) for v in row] for row in [x.split(' ') for x in lines[2].split('\n')[1:]]]
    fert2watr = [[int(v) for v in row] for row in [x.split(' ') for x in lines[3].split('\n')[1:]]]
    watr2lght = [[int(v) for v in row] for row in [x.split(' ') for x in lines[4].split('\n')[1:]]]
    lght2temp = [[int(v) for v in row] for row in [x.split(' ') for x in lines[5].split('\n')[1:]]]
    temp2humd = [[int(v) for v in row] for row in [x.split(' ') for x in lines[6].split('\n')[1:]]]
    humd2loct = [[int(v) for v in row] for row in [x.split(' ') for x in lines[7].split('\n')[1:]]]

def lkp(seed_nr,lkp):
    match = 0
    for i in lkp:
        if seed_nr-i[2] < i[1] and seed_nr >= i[1]:
            match = 1
            deltaFromStart = seed_nr - i[1]
            return i[0]+deltaFromStart
    if match == 0:
        return seed_nr
min = 9999999999
for i in range(0,len(seeds)):
    print(seeds[i])
    location = lkp(lkp(lkp(lkp(lkp(lkp(lkp(seeds[i],seed2soil),soil2fert),fert2watr),watr2lght),lght2temp),temp2humd),humd2loct)
    if location < min:
        min = location

print('Part 1: '+ str(min))

first = 1
min = 9999999999
for i in range(0,len(seeds)):
    if first == 1:
       start = seeds[i]
       first = 0
    else:
        for seed in list(range(start,start + seeds[i])):
            location = lkp(lkp(lkp(lkp(lkp(lkp(lkp(seed,seed2soil),soil2fert),fert2watr),watr2lght),lght2temp),temp2humd),humd2loct)
            if location < min:
                min = location
        first = 1

print('Part 2: '+ str(min))
