print(chr(27)+'[2j')
print('\033c')

RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
LIGHT_BLUE_BG = "\033[104m"

f = open('25.test', 'r')
f = open('25.input', 'r')
lines = [x.strip() for x in f.read().strip().split('\n\n')]

lock_schematics = []
key_schematics = []
for line in lines:
    thing = line.split('\n')
    if thing[0] == '#####':
        lock_schematics.append(thing)
    if thing[-1] == '#####':
        key_schematics.append(thing)

def parse(thing):
    a,b,c,d,e = [-1,-1,-1,-1,-1]
    print()
    for l in thing:
        a += 1 if l[0] == '#' else 0
        b += 1 if l[1] == '#' else 0
        c += 1 if l[2] == '#' else 0
        d += 1 if l[3] == '#' else 0
        e += 1 if l[4] == '#' else 0
    return (a,b,c,d,e)



print('-'*10, 'Locks')
locks = []
for lock in lock_schematics:
    locks.append(parse(lock))
    print(locks[-1])

print('-'*10, 'Keys')
keys = []
for key in key_schematics:
    keys.append(parse(key))
    print(keys[-1])


def overlap(lock, key):
    for i in range(5):
        s = lock[i]+key[i]
        if s > 5:
            return True
    return False

count = 0
for lock in locks:
    for key in keys:
        overlaps = overlap(lock, key)
        print(f'Lock: {lock}, Key: {key}, overlaps: {overlaps}')
        if not overlaps:
            count += 1

print('Counts', count)
