with open(r'./AOC2023/D6/D6.example') as f:
    lines = f.read().split('\n')
times = [int(x) for x in lines[0].split(': ')[1].split(' ') if x != '']
distances = [int(x) for x in lines[1].split(': ')[1].split(' ') if x != '']

print(times)
print(distances)