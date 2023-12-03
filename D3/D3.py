with open(r'./AOC2023/D3/D3.data') as f:
    lines = f.read().split('\n')
print(lines)
indexOfSpecials = []
for i in range(0,len(lines)): 
    for j in range(0,len(lines[i])):
        try:
            int(lines[i][j])
        except:
            if lines[i][j] != '.':
                indexOfSpecials.append([i,j])
print(indexOfSpecials)
#indexOfSpecials = indexOfSpecials[0]
placesToLook = []
for i in indexOfSpecials:
    print(i)
    placesToLook.append(str(i[0]+1)+','+str(i[1]))
    placesToLook.append(str(i[0]+1)+','+str(i[1]+1))
    placesToLook.append(str(i[0])+','+str(i[1]+1))
    placesToLook.append(str(i[0]-1)+','+str(i[1]+1))
    placesToLook.append(str(i[0]-1)+','+str(i[1]))
    placesToLook.append(str(i[0]-1)+','+str(i[1]-1))
    placesToLook.append(str(i[0])+','+str(i[1]-1))
    placesToLook.append(str(i[0]+1)+','+str(i[1]-1))
placesToLook = list(set(placesToLook))
print('Finished Finding the places to look for integers')
print(len(placesToLook))