f = open('01.input', 'r')
#f = open('01.test', 'r')
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
        incr = 0

        for i in range(digit):
            dial += diff
            dial = dial % 100 
            if dial == 0:
                incr += 1

        tot += incr
    return tot 


def part2_pretty(): # Or not pretty?
    dial = 50
    tot = 0
    last = 0

    for line in rows:
        direction = -1 if line[0] == 'L' else 1
        digit = int(line[1:])

        incr = abs(digit // 100)
        modulo = digit % 100
        new_value = dial + (modulo * direction)

        if new_value % 100 == 0: # 1) If we land on 0
            incr += 1
        else:
            step = new_value // 100 # 2) If we change "step"
            if step != last and (dial % 100 != 0): # 3) But weren't on 0 last.
                incr += 1
        
        last = step
        dial = new_value
        tot += incr
    return tot 

result2 = part2()
print("Part 2 solution: %d" % result2)
result2 = part2_pretty()
print("Part 2 solution: %d" % result2)

# 2431
# 2841
# 6908
# 6283
