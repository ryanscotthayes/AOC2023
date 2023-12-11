import numpy as np

with open(r'./AOC2023/D9/D9.data') as f:
    lines = [x.split(' ') for x in f.read().split('\n')]

data = []
for i in lines:
    intermed = []
    for j in i:
        intermed.append(int(j))
    data.append(intermed)

answer,answer2 = 0,0
answerArray = []
for item in data:
    poly = np.polynomial.polynimial.Polynomial.fit(np.arange(len(item)),item,deg=len(item)-1)
    answerArray.append([round(poly(len(item))),round(poly(-1))])
    answer += round(poly(len(item)))
    answer2 += round(poly(-1))

print('Part 1: '+ str(answer))
print('Part 2: '+ str(answer2))