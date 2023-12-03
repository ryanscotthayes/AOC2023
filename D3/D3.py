def checkIfInt(array,source_data):
    if source_data[array[0]][array[1]].isdigit():
        currentPos = [array[0],array[1]]
        currentCheck = source_data[array[0]][array[1]]
        while currentCheck.isdigit():
            currentPos = [currentPos[0],currentPos[1]-1]
            currentCheck = lines[currentPos[0]][currentPos[1]]
        return str(currentPos[0])+','+str(currentPos[1]+1)

with open(r'./AOC2023/D3/D3.data') as f:
    lines = f.read().split('\n')
indexOfSpecials = []
for i in range(0,len(lines)): 
    for j in range(0,len(lines[i])):
        try:
            int(lines[i][j])
        except:
            if lines[i][j] != '.':
                indexOfSpecials.append([i,j])
#indexOfSpecials = indexOfSpecials[0]
placesToLook = []
for i in indexOfSpecials:
    placesToLook.append(str(i[0]+1)+','+str(i[1]))
    placesToLook.append(str(i[0]+1)+','+str(i[1]+1))
    placesToLook.append(str(i[0])+','+str(i[1]+1))
    placesToLook.append(str(i[0]-1)+','+str(i[1]+1))
    placesToLook.append(str(i[0]-1)+','+str(i[1]))
    placesToLook.append(str(i[0]-1)+','+str(i[1]-1))
    placesToLook.append(str(i[0])+','+str(i[1]-1))
    placesToLook.append(str(i[0]+1)+','+str(i[1]-1))
placesToLook = list(set(placesToLook))
surroundSpecials = []
for i in placesToLook:
    surroundSpecials.append([int(x) for x in i.split(",")])

enginePartLocations = []
for i in surroundSpecials:
    try: #check if integer
        int(lines[i[0]][i[1]])
        enginePartLocations.append([i[0],i[1]])
    except:
        pass

engineLocationStartsString = []
for i in enginePartLocations:
    currentPos = [i[0],i[1]]
    currentCheck = lines[i[0]][i[1]]
    while currentCheck.isdigit():
        currentPos = [currentPos[0],currentPos[1]-1]
        currentCheck = lines[currentPos[0]][currentPos[1]]
    engineLocationStartsString.append(str(currentPos[0])+','+str(currentPos[1]+1))

engineLocationStartsString = list(set(engineLocationStartsString))
engineLocationStarts = []
for i in engineLocationStartsString:
    engineLocationStarts.append([int(x) for x in i.split(",")])
sumPartNums = 0
for i in engineLocationStarts:
    string = lines[i[0]][i[1]:i[1]+3]
    partNumberString = ''
    for char in string:
        if char.isdigit():
            partNumberString = partNumberString + char
        else:
            break
    sumPartNums += int(partNumberString)
print('Part 1: ' + str(sumPartNums))

indexOfAsterisks = []
for i in range(0,len(lines)): 
    for j in range(0,len(lines[i])):
        try:
            int(lines[i][j])
        except:
            if lines[i][j] == '*':
                indexOfAsterisks.append([i,j])

returnGearStartsString = []
for i in indexOfAsterisks:
    round = []
    round.append(checkIfInt([i[0]+1,i[1]],lines))
    round.append(checkIfInt([i[0]+1,i[1]+1],lines))
    round.append(checkIfInt([i[0],i[1]+1],lines))
    round.append(checkIfInt([i[0]-1,i[1]+1],lines))
    round.append(checkIfInt([i[0]-1,i[1]],lines))
    round.append(checkIfInt([i[0]-1,i[1]-1],lines))
    round.append(checkIfInt([i[0],i[1]-1],lines))
    round.append(checkIfInt([i[0]+1,i[1]-1],lines))
    test = list(set([i for i in round if i is not None]))
    if len(test) == 2:
        returnGearStartsString.append(test)


returnGearStarts = []
for i in returnGearStartsString:
    returnGearStartsintermed = []
    for j in i:
        returnGearStartsintermed.append([int(x) for x in j.split(",")])
    returnGearStarts.append(returnGearStartsintermed)

gear_ratios = []
for gear in returnGearStarts:
    gear_ratio = 1
    for part in gear:
        string = lines[part[0]][part[1]:part[1]+3]
        partNumberString = ''
        for char in string:
            if char.isdigit():
                partNumberString = partNumberString + char
            else:
                break
        gear_ratio = gear_ratio*int(partNumberString)
    gear_ratios.append(gear_ratio)
print('Part 2: '+str(sum(gear_ratios)))