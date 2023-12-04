with open(r'./AOC2023/D4/D4.data') as f:
    lines = f.read().split('\n')

def listIntersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

winningNumsData,myNumsData,cardNumData = [],[],[]

for i in lines: 
    cardNum = i.split(':')[0].split(' ')[1]
    cardNumData.append(cardNum)
    winningNums = i.split(':')[1].split(' | ')[0].split(' ')    
    winningNums = [int(k) for k in winningNums if k != '']
    winningNumsData.append(winningNums)
    myNums = i.split(':')[1].split(' | ')[1].split(' ')    
    myNums = [int(k) for k in myNums if k != '']
    myNumsData.append(myNums) 
    
allWins,winningCards = [],[]
for i in range(0,len(lines)):
    winningIntersects = listIntersection(winningNumsData[i],myNumsData[i])
    winningCards.append([i+1,len(winningIntersects),1])
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
nrcards = len(winningCards)
for i in range(0,len(winningCards)):
    for j in range(0,winningCards[i][1]):
        winningCards[i+j+1][2] +=1*winningCards[i][2]
sol2 = 0
for i in winningCards:
    sol2+=i[2]
print('Part 2: ' +str(sol2))