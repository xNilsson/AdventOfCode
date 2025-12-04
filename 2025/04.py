print(chr(27)+'[2j')
print('\033c')
f = open('04.test', 'r')
f = open('04.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

grid = []
rolls_left = set()
for y, line in enumerate(lines):
    grid.append([])
    for x, l in enumerate(line):
        grid[y].append(l)
        if l == '@':
            rolls_left.add((x,y))

def can_access(rolls_left, x,y):
    neighbour = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue

            nx, ny = x + dx, y + dy
            if (nx,ny) in rolls_left:
                neighbour += 1
    return neighbour

# For debugging
def print_map(grid, rolls):
    for y, line in enumerate(grid):
        for x, a in enumerate(line):
            if (x,y) in rolls:
                grid[y][x] = 'x'
        print(''.join(grid[y]))

def get_rolls(rolls_left):
    rolls = [] 
    for (x,y) in rolls_left:
        ns = can_access(rolls_left, x,y)
        if ns < 4:
            rolls.append((x,y))

    for (x,y) in rolls:
        if (x,y) in rolls_left:
            rolls_left.remove((x,y))
    return rolls, rolls_left



i = 0
rolls_moved = set()
while True:
    rolls, rolls_left = get_rolls(rolls_left)
    #print_map(grid, rolls)

    if i == 0:
        print('-- Part 1:', len(rolls))

    if len(rolls) == 0:
        break

    rolls_moved |= set(rolls)
    print(f'{i} => Current: {len(rolls_moved)}')
    i += 1

print('Part 2:', len(rolls_moved))

t2 = perf_counter()
print('Time:', t2 - t1)
