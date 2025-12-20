from functools import lru_cache
from random import choices
import heapq
print(chr(27)+'[2j')
print('\033c')
f = open('10.test', 'r')
f = open('10.input', 'r')
lines = [x.strip() for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()


# This day broke me :( tried so many search algorithms, 
# eventually needed to use z3 and ask for help...


def parse(line):
    diagram = line.split('[')[1].split(']')[0]
    btns = [
         [int(x) for x in a.split(')')[0].split(',')]
        for a
        in line.split('(')[1:]
    ]
    joltage = [
         int(x)
        for x 
        in line.split('{')[1].split('}')[0].split(',')
    ]
    return diagram, btns, joltage


# res1 = 0
# for line in lines:
#     diagram, btns, joltage = parse(line)
#     q = []
#     current = ''.join(['.' for x in diagram])
#     q.append((0, [], current))
#     idx = 0
#     visited = set()
#     while len(q) > 0:
#         count, path, current = q.pop(0)
#         if diagram == current:
#             break
# 
#         if current in visited:
#             continue
#         visited.add(current)
# 
#         for btn in btns:
#             nxt = [x for x in current]
#             for i in btn:
#                 nxt[i] = '.' if nxt[i] == '#' else '#'
#             new_path = [x for x in path]
#             new_path.append(btn)
#             q.append((count+1, new_path, ''.join(nxt)))
# 
#         q = sorted(list(q))
#     res1 += len(path)
# 
# print('🏆 Solution part1:', res1)
        

count = 0

# @lru_cache
# def rec(joltage, btns, clicks, curr_win):
#     global count
#     #print(joltage, btns, clicks)
# 
#     count += 1
#     if count % 1000000 == 0:
#         print(f'{count} --> {clicks} ')
#     #if count > 500:
#     #    exit()
# 
#     all_zero = True
#     max_j = 0
#     for x in joltage:
#         if x != 0:
#             all_zero = False
#         max_j = max(max_j, x)
#     if all_zero:
#         print('FOUND', clicks)
#         return True, clicks
# 
#     if len(btns) == 0:
#         return False, curr_win
# 
#     btn = btns[0]
#     rest = tuple(btns[1:])
# 
#     least_clicks = curr_win
#     did_win = False
#     for i in range(max_j+1, -1, -1):
#         if (clicks+i) >= curr_win:
#             continue
# 
#         new_joltage = [x for x in joltage]
#         is_valid = True
#         for v in btn:
#             new_joltage[v] -= i
#             if new_joltage[v] < 0:
#                 is_valid = False
#         if not is_valid:
#             continue
# 
#         #print(f'BTN {btn} --> i: {i}')
# 
#         win, new_clicks = rec(tuple(new_joltage), rest, clicks+i, curr_win)
#         if win:
#             did_win = True
#             curr_win = new_clicks
#             if new_clicks == max_j:
#                 return True, new_clicks
#         if new_clicks < least_clicks:
#             least_clicks = new_clicks
#     return did_win, least_clicks 


def dot_prod(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))



from z3 import *

def min_press(buttons, target, mode="mod2"):
    """
    buttons: list[list[int]]
    target: list[int]
    mode: "mod2" (Part 1) or "linear" (Part 2)
    """
    m = len(buttons)
    n = len(target)

    opt = Optimize()

    # x_j = number of times button j is pressed
    x = [Int(f"x_{j}") for j in range(m)]

    # x_j >= 0
    for xj in x:
        opt.add(xj >= 0)

    # joltage counters
    for i in range(n):
        expr = Sum([x[j] for j in range(m) if i in buttons[j]])
        opt.add(expr == target[i])

    # Minimize total presses
    total_presses = Sum(x)
    opt.minimize(total_presses)

    if opt.check() != sat:
        raise RuntimeError("No solution")

    model = opt.model()
    return sum(model[xj].as_long() for xj in x)


res2 = 0
from collections import Counter
c = Counter()
for line in lines:
    print('====================================')
    diagram, btns, joltage = parse(line)
    joltage = tuple(joltage)
    max_jolt = max(joltage)
    print(f'JOLTAGE: {joltage}')
    print(f'-- Buttons ---')
    for b in btns:
        print(b)
    print(f'-- ---')
    btns = sorted(btns, key=len)
    btns.reverse()
    btns = tuple([tuple(x) for x in btns])

    res = min_press(btns, joltage)
    print('RES:', res)
    res2 += res 
    continue

    
    btns = [
        [1 if i in btn else 0 for i,_ in enumerate(joltage)]
        for btn
        in btns
    ]


    steps = [0 for b in btns]
    start = [0 for x in joltage]
    goal = [x for x in joltage]
    print(f'Start: {start}, goal: {goal}, steps: {steps}')
    

    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start, steps))
    visited = set()
    count = 0
    while len(q) > 0:
        h, start, steps = heapq.heappop(q)
        count += 1
        if count > 40:
            break
        if count % 10000 == 0:
            print(count, '🍏 NXT: ', h, start, steps)

        v = [b - a for (a,b) in zip(start,goal)]
        if sum([abs(x) for x in v]) == 0:
            print('FOUND!!', v)
            exit()
            break

        closest = 0
        nxt = 0
        to_add = True
        for idx, b in enumerate(btns):
            new_start = tuple([s + b[i] for i,s in enumerate(start)])
            dot = dot_prod(new_start, v)
            if abs(dot) > closest and new_start not in visited:
                to_add = True 
                nxt = idx
                start_to_add = new_start

            if steps[idx] <= 0:
                continue

            new_start = tuple([s - b[i] for i,s in enumerate(start)])
            dot = dot_prod(new_start, v)
            if abs(dot) > closest and new_start not in visited:
                to_add = False
                nxt = idx
                start_to_add = new_start

        if to_add:
            steps[nxt] += 1
        else:
            steps[nxt] -= 1

        print(f'{start_to_add} -- Steps: {steps} --> {nxt} {to_add}')
        visited.add(start_to_add)
        heapq.heappush(q, (0, start_to_add, steps))
        

        #exit()



    exit()

    max_presses = sum(joltage)
    gen0 = [max_presses // len(btns) for b in btns]
    for i in range(max_presses % len(btns)):
        gen0[i] += 1
    print('max presses:', max_presses)
    print(f'gen0: {gen0}')

    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, 0, gen0))
    idx = 0
    visited = set()
    min_count = 99999
    while len(q) > 0:
        idx += 1
        left, count, current = heapq.heappop(q)
        if count > min_count:
            continue
        if idx % 10000 == 0:
            print(idx, '🍏 NXT: ', count, len(q), current, len(visited) , left)
            #exit()


        v = [j for j in joltage]
        # Process
        for btn_idx, presses in enumerate(current):
            if presses == 0:
                continue
            btn = btns[btn_idx]
            for v_idx in btn:
                v[v_idx] -= presses
        diff = sum([abs(i) for i in v])
        # print(idx, '🍏 NXT: ', count, current, joltage, diff)
        # print(f'Joltage: {joltage}')
        # print(f'Current: {current}')
        # print(f'btns: {btns}')
        # print(f'v: {v}')
        # print(f'diff: {diff}')

        if diff == 0:
            print('NEW MIN', count)
            min_count = count
            continue

        # Weight
        idxs = []
        weights = []
        min_w = 9999
        for btn_idx, presses in enumerate(current):
            weight = 0
            btn = btns[btn_idx]
            for v_idx in btn:
                weight += v[v_idx]
            idxs.append((btn_idx,presses))
            weights.append(weight)
            min_w = min(min_w, weight)
        weights = [w - min_w + 1 for w in weights]

        for (btn_idx, presses) in choices(idxs, weights, k=5):

            weight = weights[btn_idx]
            new_gen = [x for x in current]
            [change] = choices([1,2,3,4,5], k=1)
            if weight > 0:
                new_gen[btn_idx] -= change
                if new_gen[btn_idx] < 0:
                    continue
            if weight < 0:
                new_gen[btn_idx] += change

            count = sum(new_gen)
            new_gen = tuple(new_gen)

            if new_gen in visited:
                continue
            visited.add(new_gen)

            heapq.heappush(q, (diff, count, new_gen))


    print('Min_count', min_count)


    exit()

    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, 0, joltage))
    idx = 0
    visited = set()
    min_count = 999999999
    closest = 99999
    while len(q) > 0:
        idx += 1
        left, count, current = heapq.heappop(q)
        if count > min_count:
            print('loool', count)
            continue
        if idx % 10000 == 0:
            print(idx, '🍏 NXT: ', count, len(q), current, len(visited), closest )

        closest = min(sum(current), closest)
        if sum(current) == 0:
            print('mincount', count)
            min_count = count
            continue

        i1, v1 = 0,0
        for i,v in enumerate(current):
            if v > v1:
                v1 = v
                i1 = i
        i2, v2 = 0,0
        for i,v in enumerate(current):
            if v > v2 and v != v1:
                v2 = v
                i2 = i

        to_press = max(v1 - v2, 1)

        #print(f'idx of max: {i1} with {v1}. To press = {to_press}')
        for btn in btns:
            if i1 not in btn:
                continue

            #print(f'Btn: {btn}')
            for diff in range(0,to_press+1):
                nxt = [x for x in current]

                valid = True
                for x in btn:
                    nxt[x] -= diff 
                    if nxt[x] < 0:
                        valid = False
                if not valid:
                    continue

                nxt = tuple(nxt)
                if nxt in visited:
                    continue
                visited.add(nxt)

                #print(f'ADD: {nxt}')
                heapq.heappush(q, (count+diff, count+diff, tuple(nxt)))

    print('RES:', min_count)
    res2 += min_count 
    exit()

print('🏆 Solution part2:', res2)




t2 = perf_counter()
print('Time:', t2 - t1)
