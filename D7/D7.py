with open(r'./AOC2023/D7/D7.data') as f:
    lines = f.read().split('\n')

def handScore(hand,part=1):
    lookupvalues = {
        'A':'A','K':'B','Q':'C','J':'D','T':'E','9':'F','8':'G','7':'H','6':'I','5':'J','4':'K','3':'L','2':'M'
        }
    output = ''
    if part == 1:
        for letter in hand:
            if letter in lookupvalues:
                output+=lookupvalues[letter]
        return output
    else:
        for letter in hand:
            if letter == 'J':
                output+='N'
            elif letter in lookupvalues:
                output+=lookupvalues[letter]
        return output

def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    return sub_li


hands = [x.split(' ')[0] for x in lines]
bids = [int(x.split(' ')[1]) for x in lines]

scores,scores2 = [],[]

for i in hands:
    score = ''
    flag,hasJokers = 0,0
    Acnt = i.count('A')
    Kcnt = i.count('K')
    Qcnt = i.count('Q')
    Jcnt = i.count('J')
    Tcnt = i.count('T')
    cnt9 = i.count('9')
    cnt8 = i.count('8')
    cnt7 = i.count('7')
    cnt6 = i.count('6')
    cnt5 = i.count('5')
    cnt4 = i.count('4')
    cnt3 = i.count('3')
    cnt2 = i.count('2')
    nrDistinct = len(list(set(i)))
    max_counts = max(Acnt,Kcnt,Qcnt,Jcnt,Tcnt,cnt9,cnt8,cnt7,cnt6,cnt5,cnt4,cnt3,cnt2)
    max_counts2 = max(Acnt,Kcnt,Qcnt,Tcnt,cnt9,cnt8,cnt7,cnt6,cnt5,cnt4,cnt3,cnt2)
    if Jcnt > 0:
        hasJokers = 1

    if max_counts == 5: #5 of kind
        score = 'A'
    elif max_counts == 4: # 4 of kind
        score = 'B'
    elif max_counts == 3 and nrDistinct == 2: #Full house
        score = 'C'
    elif max_counts == 3 and nrDistinct == 3: #3ofkind
        score = 'D'
    elif max_counts == 2 and nrDistinct == 3: #2pair
        score = 'E'
    elif max_counts == 2: #1pair
        score = 'F'
    elif nrDistinct == 5: #High Card
        score = 'G'
    
    if max_counts2+Jcnt == 5:
        score2 = 'A'
    elif max_counts2+Jcnt == 4: # 4 of kind
        score2 = 'B'
    elif max_counts2+Jcnt == 3 and nrDistinct - hasJokers == 2: #Full house
        score2 = 'C'
    elif max_counts2+Jcnt == 3 and nrDistinct - hasJokers == 3: #3ofkind
        score2 = 'D'
    elif max_counts2+Jcnt == 2 and nrDistinct - hasJokers == 3: #2pair
        score2 = 'E'
    elif max_counts2+Jcnt == 2: #1pair
        score2 = 'F'
    elif nrDistinct == 5: #High Card
        score2 = 'G'
  
    handValue = handScore(i)
    handValue2 = handScore(i,2)
    scores.append(score+handValue)
    scores2.append(score2+handValue2)

scoreBids = []
for i in range(0,len(scores)):
    scoreBids.append([bids[i],scores[i]])
scoreBids = Sort(scoreBids)
winnings = 0
for i in range(0,len(scoreBids)):
    rank = len(scoreBids) - i
    winnings += rank*scoreBids[i][0]

print('Pt 1: ' + str(winnings))

scoreBids2 = []
for i in range(0,len(scores2)):
    scoreBids2.append([bids[i],scores2[i]])
scoreBids2 = Sort(scoreBids2)
winnings2 = 0
for i in range(0,len(scoreBids2)):
    rank2 = len(scoreBids2) - i
    winnings2 += rank2*scoreBids2[i][0]


print('Pt 2: ' + str(winnings2))