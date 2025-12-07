print(chr(27)+'[2j')
print('\033c')
f = open('07.input', 'r')
f = open('07.test', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

def parse(lines):
    grid = {}
    start = None
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            grid[(x,y)] = letter
            if letter == 'S':
                start = (x,y)
    return grid, start

def part1(start, grid):
    beams = set()
    beams.add((start))
    res = 0
    while len(beams) > 0:
        beam = beams.pop()
        x,y = beam
        nxt = (x, y+1)
        if nxt not in grid:
            continue
        if grid[nxt] == '^':
            res += 1 
            beams.add((x-1, y))
            beams.add((x+1, y))
            grid[(x-1,y)] = '|'
            grid[(x+1,y)] = '|'
            
        if grid[nxt] == '.':
            beams.add(nxt)
            grid[nxt] = '|'
    return res
        
from functools import cache

@cache
def paths(beam):
    global grid
    x,y = beam
    nxt = (x, y+1)
    if nxt not in grid:
        return 1
    if grid[nxt] == '^':
        lft = paths((x-1, y))
        rgt = paths((x+1, y))
        return lft + rgt 
        
    if grid[nxt] == '.':
        return paths(nxt) 
    return 1

def part2(grid, start):
    return paths(start)

grid , start = parse(lines)
print('Part 1:', part1(start, grid))
grid , start = parse(lines)
print('Part 2:', part2(grid, start))



t2 = perf_counter()
print('Time:', t2 - t1)
