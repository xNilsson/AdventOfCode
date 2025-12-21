from functools import cache
import math
print(chr(27)+'[2j')
print('\033c')
f = open('12.test', 'r')
f = open('12.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

done = set() 
connections = {}


regions = []
shapes = {}
idx = 0
for line in lines: 
    if 'x' in line:
        size, indexes = line.split(': ')
        w,h = size.split('x')
        regions.append((int(w), int(h), [int(x) for x in indexes.split()]))
        continue

    if line == '':
        shapes[idx] = [shape]

        continue

    if ':' in line:
        idx = int(line[:-1])
        row = 0
        shape = []
        continue

    for col, c in enumerate(line):
        if c == '#':
            shape.append((col, row))

    row += 1

sizes = {}
for idx in shapes:
    identity = shapes[idx][0]
    sizes[idx] = len(identity)

count = 0
for r in regions:
    w,h,idxs = r
    tot = w*h
    covers = 0
    for idx, shape_count in enumerate(idxs):
        covers += sizes[idx] * shape_count
    if tot <= covers:
        continue

    print(f'🟢 region {r} =>> {tot}, covers: {covers}')
    count += 1

print(f'sizes {sizes}')
print(f'count {count}')

t2 = perf_counter()
print(f'Time: {int(1000*(t2 - t1))}ms')
