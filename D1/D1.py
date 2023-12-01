import re
with open(r'./AOC2023/D1/D1.data') as f:
    lines = f.read().split('\n')

def stringParser(string):
    returnArray = []
    for j in range(0,len(string)):
        try:
            if int(string[j]) > 0:
                returnArray.append(int(string[j]))
        except:
            if string[j:j+3] == 'one':
                returnArray.append(1)
            elif string[j:j+3] == 'two':
                returnArray.append(2)
            elif string[j:j+5] == 'three':
                returnArray.append(3)
            elif string[j:j+4] == 'four':
                returnArray.append(4)
            elif string[j:j+4] == 'five':
                returnArray.append(5)
            elif string[j:j+3] == 'six':
                returnArray.append(6)
            elif string[j:j+5] == 'seven':
                returnArray.append(7)
            elif string[j:j+5] == 'eight':
                returnArray.append(8)
            elif string[j:j+4] == 'nine':
                returnArray.append(9)
    return returnArray


try:
    sol = 0
    for i in lines:
        a = re.sub(r'[A-z]*', '', i)
        digits = int(a[0]+a[-1:])
        sol+=digits

    print('Part 1:' + str(sol))
except:
    pass

sol2 = 0
for i in lines:
    a = stringParser(i)
    print(a)
    digits = int(str(a[0])+str(a[-1]))
    sol2+=digits

print('Part 2:' + str(sol2))