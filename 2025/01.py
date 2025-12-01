#f = open('01.input', 'r')
f = open('01.test', 'r')
content = [x.strip() for x in f.readlines()]
rows = [str(x) if x != '' else '' for x in content]


def part1():
    dial = 50
    tot = 0

    for line in rows:
        digit = int(line[1:])
        if line.startswith('L'):
            dial -= digit
        else:
            dial += digit
        dial = dial % 100 
        #print('The dial is rotated ', line,' to point at ', dial)

        if dial == 0:
            tot += 1
    return tot 

result1 = part1()
print("Part 1 solution: %d" % result1)

def part2():
    dial = 50
    tot = 0

    for line in rows:
        digit = int(line[1:])
        diff = -1 if line.startswith('L') else 1
        passed = 0
        incr = 0

        for i in range(digit):
            dial += diff
            dial = dial % 100 
            if dial == 0:
                incr += 1
                if i < (digit-1):
                    passed += 1

        #if passed > 0:
        #    print(f'The dial is rotated {line} to point at {dial}; during this rotation, it points at 0: {passed} times.')
        #else:
        #    print(f'The dial is rotated {line} to point at {dial};')

        tot += incr
    return tot 

result2 = part2()
print("Part 2 solution: %d" % result2)

# 2431
# 2841
# 6908
# 6283
