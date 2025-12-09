import heapq
import math
print(chr(27)+'[2j')
print('\033c')
f = open('08.test', 'r')
f = open('08.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

boxes = [] 
for line in lines:
    box = [int(x) for x in line.split(',')]
    boxes.append(tuple(box))

ds = []
dmap = {}
for i1, p1 in enumerate(boxes):
    for i2, p2 in enumerate(boxes):
        if i1 == i2: 
            continue
        d = math.sqrt(
            pow(p2[0]-p1[0], 2) + 
            pow(p2[1]-p1[1], 2) + 
            pow(p2[2]-p1[2], 2)
        )
        if (p2,p1) in dmap:
            continue
        dmap[(p1,p2)] = d
        ds.append((d,p1,p2))

def part1(circuits):
    sizes = [len(x) for x in circuits]
    sizes = sorted(sizes)
    tot = 1
    for s in sizes[-3:]:
        tot *= s
    return tot


heapq.heapify(ds)
circuits = []
for b in boxes:
    s = set()
    s.add(b)
    circuits.append(s)

idx = 0
last_x = [0,0]
while len(circuits) > 1:
    idx+=1
    print('Idx', idx)
    d, p1, p2 = heapq.heappop(ds)
    i1 = -1
    i2 = -1
    for i, g in enumerate(circuits):
        if p1 in g:
            i1 = i
        if p2 in g:
            i2 = i
    assert(i1 != -1)
    assert(i2 != -1)

    last_x = [p1[0], p2[0]]
    if i1 != i2:
        for p in circuits[i2]:
            circuits[i1].add(p)
        del circuits[i2]

    if idx == 10:
        res1 = part1(circuits)
    if idx == 1000:
        res1 = part1(circuits)

print('part1:', res1)
print('part2:', last_x[0] * last_x[1])


t2 = perf_counter()
print('Time:', t2 - t1)
