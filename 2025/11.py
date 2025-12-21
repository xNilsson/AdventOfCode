from functools import cache
import math
print(chr(27)+'[2j')
print('\033c')
f = open('11.test', 'r')
f = open('11.test2', 'r')
f = open('11.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

done = set() 
connections = {}

for line in lines: 
    start, end = line.split(': ')
    end = end.split()
    connections[start] = end

# @cache
# def solve_1(path, curr):
#     global connections
#     #print('SOLVE:', path, curr)
#     path = list(path)
#     path.append(curr)
#     path = tuple(path)
#     if curr == 'out':
#         return [path]
# 
# 
#     nxts = connections[curr]
#     paths = []
#     for nxt in nxts:
#         if nxt in path:
#             continue
#         nxt_paths = solve_1(path, nxt)
#         paths.extend(nxt_paths)
#     return paths 
# 
# paths = solve_1(tuple([]), 'you')
# 
# # print('------- PATHS')
# # for p in paths:
# #     print('--', p)
# # print('-------')
# 
# res1 = len(paths)
# print('🏆 Solution part1:', res1)


back = {}

for a in connections:
    print(a, connections[a])
    for b in connections[a]:
        if b not in back:
            back[b] = set()
        back[b].add(a)

first_back = {x: set(list(back[x])) for x in back}


adding = True
while adding:
    adding = False
    new_back = { x: set(list(back[x])) for x in back}
    for a in back:
        for b in back[a]:
            if b not in back:
                continue
            for c in back[b]:
                if c in back[a]:
                    continue
                adding = True
                new_back[a].add(c)

    back = { x: set(list(new_back[x])) for x in new_back}
print('--- PREPARATION DONE')

#import heapq
from collections import deque
def solve_3(start, end, must_have):
    global connections, count, max_len, back

    print(f'➡️ SOLVE: {start} -> {end}')

    q = deque()
    q.append((start, [start]))
    paths = set() 
    count = 0
    dead_ends = set()
    for m in must_have:
        dead_ends.add(m)

    # Find all dead ends
    for c in connections:
        if c not in back:
            continue
        can_go = back[c]
        is_valid = True
        for m in must_have:
            if m not in can_go:
                is_valid = False
                break
        if c != end and end not in can_go:
            is_valid = False

        if not is_valid:
            dead_ends.add(c)

    
    local_first_back = {}
    for node in first_back:
        local_first_back[node] = set()
        for x in first_back[node]:
            if x in dead_ends:
                continue
            local_first_back[node].add(x)


    while len(q) > 0:
        curr, path = q.popleft()

        count += 1
        if count % 100000 == 0:
            print(f'{count}:: {len(q)}, {len(paths)}')

        for prev in local_first_back[curr]:
            #if prev in dead_ends:
            #    continue
            if prev in path: # Already visited
                continue
            if prev == end:
                path = list(path)
                path.append(prev)
                paths.add(tuple(path))
                continue
            new_path = [x for x in path]
            new_path.append(prev)
            q.append((prev, new_path))

    
    return len(paths)
    
res1 = solve_3('out', 'dac', ['fft', 'svr'])
print('🏆 out --> dac:', res1)
res3 = solve_3('fft', 'svr', [])
print('🏆 fft --> svr:', res3)
res2 = solve_3('dac', 'fft', ['svr'])
print('🏆 dac --> fft:', res2)
also = res1 * res2 * res3
print('🏆🏆🏆🏆 TOT:', also)
res1 = solve_3('out', 'fft', ['dac', 'svr'])
print('🏆 out -> fft:', res1)
if res1 == 0:
    exit()
res2 = solve_3('fft', 'dac', ['svr'])
print('🏆 fft -> dac:', res2)
if res2 == 0:
    exit()
res3 = solve_3('dac', 'svr', [])
print('🏆 dac -> svr:', res3)
either = res1 * res2 * res3
print('🏆🏆🏆🏆 TOT:', either)
print('🏆🏆🏆🏆🏆🏆🏆🏆 TOT:', also + either)

t2 = perf_counter()
print('Time:', t2 - t1)
