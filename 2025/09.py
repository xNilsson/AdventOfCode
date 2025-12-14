import heapq
import math
print(chr(27)+'[2j')
print('\033c')
f = open('09.test', 'r')
f = open('09.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

max_area = 0
squares = []
for line in lines:
    a = tuple([int(x) for x in line.split(',')])
    for line in lines:
        b = tuple([int(x) for x in line.split(',')])
        if a == b:
            continue

        dx = abs(b[0]-a[0])+1
        dy = abs(b[1]-a[1])+1
        area = dx * dy
        max_area = area if area > max_area else max_area
        squares.append((area, a,b))

print('🏆 Solution part1:', max_area)


def inside(square, p):
    area, a, b = square
    x,y = p

    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])
    inside_x = min_x < x and x < max_x
    inside_y = min_y < y and y < max_y
    is_inside = inside_x and inside_y
    return is_inside


count = 0
points = set()
corners = set()
squares = set(squares)
lines.append(lines[0])
for (a,b) in zip(lines, lines[1:]):
    a = tuple([int(x) for x in a.split(',')])
    b = tuple([int(x) for x in b.split(',')])
    corners.add(a)
    corners.add(b)

    dx = b[0]-a[0]
    dy = b[1]-a[1]
    direction = (
        0 if b[0] == a[0] else int(dx / abs(dx)),
        0 if b[1] == a[1] else int(dy / abs(dy)),
    )
    distance = dx + dy
    for i in range(abs(distance)+1):
        point = (
            a[0] + (i * direction[0]),
            a[1] + (i * direction[1])
        )

        points.add(point)

squares = sorted(list(squares))
squares = squares[::-1]
print('✅ Sorted square list')
print('🐍 Square count', len(squares))

res2 = None
for idx, square in enumerate(squares):
    if idx % 10000 == 0:
        print(f'➡️➡️➡️➡️ Square {idx}:', square)
    to_add = True

    for point in corners:
        if inside(square, point):
            to_add = False
            break

    if to_add:
        for point in points:
            if inside(square, point):
                to_add = False
                break

    if to_add:
        res2 = square[0]
        break
print('🏆 Solution part2:', res2)

t2 = perf_counter()
print('Time:', t2 - t1)
