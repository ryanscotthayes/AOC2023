import re
with open(r'./AOC2023/D6/D6.data') as f:
    lines = f.read().split('\n')
times = [int(x) for x in lines[0].split(': ')[1].split(' ') if x != '']
distances = [int(x) for x in lines[1].split(': ')[1].split(' ') if x != '']

raceWinRecords = []
for i in range(0,len(times)):
    numWins = 0
    for j in range(0,times[i]+1):
        #j is how long youre holding button
        if (times[i]-j)*j > distances[i]:
            numWins +=1
    raceWinRecords.append(numWins)

pt1Answer = 1
for i in raceWinRecords:
    pt1Answer = pt1Answer*i

print('Part 1: '+str(pt1Answer))

times = int(re.sub(' ','',lines[0].split(': ')[1]))
distances = int(re.sub(' ','',lines[1].split(': ')[1]))

numWins = 0
raceWinRecords2 = []
for j in range(0,times+1):
    #j is how long youre holding button
    if (times-j)*j > distances:
        numWins +=1
raceWinRecords2.append(numWins)

pt2Answer = 1
for i in raceWinRecords2:
    pt2Answer = pt2Answer*i

print('Part 2: '+str(pt2Answer))