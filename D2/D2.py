import re
with open(r'./AOC2023/D2/D2.data') as f:
    lines = f.read().split('\n')

processData1 = []
for i in lines:
    processData1.append(i.split(':'))

data = []
for i in processData1:
    data.append([i[0],i[1].split(';')])

nr_reds = 12
nr_greens = 13
nr_blues = 14

failures = []
maximums = []
for i in range(0,len(data)):
    max_red = 0
    max_blue = 0
    max_green = 0
    for j in range(0,len(data[i][1])):
        redShown = re.findall(' [0-9]* red',data[i][1][j])
        reds = sum([int(re.sub('[A-z ]','',i)) for i in redShown])
        blueShown = re.findall(' [0-9]* blue',data[i][1][j])
        blues = sum([int(re.sub('[A-z ]','',i)) for i in blueShown])
        greenShown = re.findall(' [0-9]* green',data[i][1][j])
        greens = sum([int(re.sub('[A-z ]','',i)) for i in greenShown])
        if reds > max_red:
            max_red = reds
        if blues > max_blue:
            max_blue = blues
        if greens > max_green:
            max_green = greens
        if reds > nr_reds:
            failures.append([data[i][0],'red'])
        elif blues > nr_blues:
            failures.append([data[i][0],'blue'])
        elif greens > nr_greens:
            failures.append([data[i][0],'green'])
    maximums.append(max_red*max_blue*max_green)

passes = []
for i in range(0,len(data)):
    roundNumber = int(re.sub('[^0-9]*','',data[i][0]))
    if roundNumber in [int(re.sub('[^0-9]*','',xyz[0]))for xyz in failures]:
        pass # in the failure list
    else:
        passes.append(roundNumber)

print('Round 1: '+ str(sum(passes)))
print('Round 2: '+ str(sum(maximums)))


