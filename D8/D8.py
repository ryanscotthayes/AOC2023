import re
from math import gcd

with open(r'./AOC2023/D8/D8.data') as f:
    lines = f.read().split('\n')
instructions = list(lines[0])
rawmap = [re.sub('[\(\)]','',x).split(' = ') for x in lines[2:]]
map = []
for i in rawmap:
    map.append([i[0],i[1].split(', ')])


def search(instList,map,currentPos = 'AAA'):
    counter = 0
    while True:
        for i in range(0,len(instList)):
            if currentPos =='ZZZ':
                return counter
            counter+=1
            for j in range(0,len(map)):
                if currentPos == map[j][0]:
                    options = map[j][1]
            if instList[i] == 'R':
                currentPos = options[1]
            elif instList[i] == 'L':
                currentPos = options[0]
                     
        if currentPos[-1] =='Z':
                return counter


print('Part 1: '+ str(search(instructions,map,'AAA')))

output2 = []
for i in map: 
    if i[0][-1] == 'A':
        output2.append(search(instructions,map,i[0]))

lcm = 1
for i in output2:
    lcm = lcm*i//gcd(lcm, i)

print('Part 2: '+ str(lcm))