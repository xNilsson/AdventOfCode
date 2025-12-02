print(chr(27)+'[2j')
print('\033c')
f = open('02.test', 'r')
f = open('02.input', 'r')
lines = [x.strip() for x in f.readlines()]

def part1(x):
    has_found = False
    mid = len(x)//2
    a,b = x[:mid], x[mid:]
    return a == b

def part2(x):
    has_found = False
    for i in range(1, len(x)//2 + 1):
        unique = set()
        for c in range(0, len(x), i):
            chunk = x[c:c+i]
            unique.add(chunk)
        if(len(unique) == 1):
            return True
    return False

ranges = lines[0]
invalid_1 = []
invalid_2 = []
for idrange in ranges.split(','):
    start, end = idrange.split('-')
    start, end = int(start), int(end)

    for x in range(start,end+1):
        x = str(x)

        if part1(x):
            invalid_1.append(int(x))

        if part2(x):
            invalid_2.append(int(x))

res1 = sum(invalid_1)
res2 = sum(invalid_2)
print('Part 1:', res1)
print('Part 2:', res2)
