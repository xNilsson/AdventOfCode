print(chr(27)+'[2j')
print('\033c')
f = open('05.test', 'r')
f = open('05.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

def parse(lines):
    ranges = []
    ids = []
    for line in lines:
        if '-' in line:
            a,b = line.split('-')
            ranges.append((int(a) , int(b)))
            continue
        if len(line) > 0:
            ids.append(int(line))
    return ranges, ids

def part1(ranges, ids):
    count = 0
    for i in ids:
        fresh = False
        for a,b in ranges:
            if a <= i and i <= b:
                fresh = True
                break
        if fresh:
            count += 1
    return count

def part2(ranges, ids):
    is_merging = True
    while is_merging:
        is_merging = False
        new_ranges = set() 
        for a1,b1 in ranges:
            for a2,b2 in ranges:
                if (a1,b1) == (a2,b2):
                    continue
                if a2 <= a1 and a1 <= b2:
                    is_merging = True
                    a1 = a2
                if a2 <= b1 and b1 <= b2:
                    is_merging = True
                    b1 = b2
            new_ranges.add((a1,b1))
        ranges = new_ranges

    return sum([1+(b - a) for a,b in ranges])

ranges, ids = parse(lines)
print('Part 1 solution:', part1(ranges, ids))
print('Part 2 solution:', part2(ranges, ids))

t2 = perf_counter()
print('Time:', t2 - t1)
