import time
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
    #print(string)
    partNumberString = ''
    for char in string:
        if char.isdigit():
            partNumberString = partNumberString + char
        else:
            break
    sumPartNums += int(partNumberString)
print(sumPartNums)