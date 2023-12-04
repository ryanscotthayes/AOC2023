with open(r'./AOC2023/D4/D4.example') as f:
    lines = f.read().split('\n')

def listIntersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

winningNumsData = []
for i in lines: 
    winningNums = i.split(':')[1].split(' | ')[0].split(' ')    
    winningNums = [int(k) for k in winningNums if k != '']
    winningNumsData.append(winningNums)

myNumsData = []
for i in lines: 
    myNums = i.split(':')[1].split(' | ')[1].split(' ')    
    myNums = [int(k) for k in myNums if k != '']
    myNumsData.append(myNums)

allWins = []
winningCards = []
for i in range(0,len(lines)):
    winningIntersects = listIntersection(winningNumsData[i],myNumsData[i])
    winningCards.append([i+1,len(winningIntersects)])
    allWins.append(winningIntersects)

allWins = [x for x in allWins if x != []]

totalPoints = 0
for game in allWins:
    scores = 0
    for win in game:
        if scores == 0:
            scores +=1
        else:
            scores += scores
    totalPoints += scores

print('Part 1: '+str(totalPoints))
print(allWins)
print(winningCards)

copiesToAdd = []
for i in winningCards:
    for j in range(1,i[1]+1):
        copiesToAdd.append(i[0]+j)
print(copiesToAdd)

while len(copiesToAdd) != 0:
    