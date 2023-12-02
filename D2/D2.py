import re
with open(r'./AOC2023/D2/D2.data') as f:
    lines = f.read().split('\n')

processData1,data,failures,maximums,passes = [],[],[],[],[]

for i in lines:
    processData1.append(i.split(':'))

for i in processData1:
    data.append([i[0],i[1].split(';')])

for i in range(0,len(data)):
    redArray,blueArray,greenArray = [],[],[]
    for j in range(0,len(data[i][1])):
        redShown = re.findall(' [0-9]* red',data[i][1][j])
        blueShown = re.findall(' [0-9]* blue',data[i][1][j])
        greenShown = re.findall(' [0-9]* green',data[i][1][j])
        redArray.append(sum([int(re.sub('[A-z ]','',i)) for i in redShown]))
        blueArray.append(sum([int(re.sub('[A-z ]','',i)) for i in blueShown]))
        greenArray.append(sum([int(re.sub('[A-z ]','',i)) for i in greenShown]))
        if sum([int(re.sub('[A-z ]','',i)) for i in redShown]) > 12:
            failures.append([data[i][0],'red'])
        elif sum([int(re.sub('[A-z ]','',i)) for i in blueShown]) > 14:
            failures.append([data[i][0],'blue'])
        elif sum([int(re.sub('[A-z ]','',i)) for i in greenShown]) > 13:
            failures.append([data[i][0],'green'])
    maximums.append(max(redArray)*max(blueArray)*max(greenArray))

for i in range(0,len(data)):
    if int(re.sub('[^0-9]*','',data[i][0])) not in [int(re.sub('[^0-9]*','',x[0]))for x in failures]:
        passes.append(int(re.sub('[^0-9]*','',data[i][0]))) #append the round number if not in list of failures

print('Round 1: '+ str(sum(passes)))
print('Round 2: '+ str(sum(maximums)))