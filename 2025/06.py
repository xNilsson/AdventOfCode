print(chr(27)+'[2j')
print('\033c')
f = open('06.input', 'r')
f = open('06.test', 'r')
lines = [x for x in f.readlines()]

from time import perf_counter
t1 = perf_counter()

problems = {}
for line in lines:
    for idx, op in enumerate(line.split()):
        if idx not in problems:
            problems[idx] = []
        problems[idx].append(op)

tot = 0
for idx in problems:
    arr = list(reversed(problems[idx]))
    op = arr[0]
    res = 0 if op == '+' else 1
    for term in arr[1:]:
        term = int(term)
        if op == '*':
            res = res * term
        if op == '+':
            res += term

    tot += res
print('Part 1:', tot)

# =====================================================
# =====================================================
# =====================================================

# Part 2: 
# I overcomplicated the code by still dividing the columns
# from left to right, but figuring out a column with and trying to parse
# it from right to left....

start_pos = []
for i, x in enumerate(lines[-1]):
    if x != ' ':
        start_pos.append(i)
end_pos = []
for s in start_pos[1:]:
    end_pos.append(s)
end_pos.append(max([len(s) for s in lines]))


problems = {}
for idx, s in enumerate(start_pos):
    problems[idx] = []

    for line in lines:
        op = line[s:end_pos[idx]]
        problems[idx].append(op)

def empty(arr):
    for x in arr:
        if x.strip() != '':
            return False
    return True

tot = 0
for idx in problems:
    arr = list(problems[idx])
    if empty(arr):
        continue
    op = arr[-1].strip()
    terms = arr[:-1]
    terms = [list(x) for x in terms]
    res = 0 if op == '+' else 1
    max_length = max([len(x)-1 for x in terms])

    values = []
    for j in range(max_length, -1, -1):
        v = ''
        for idx in range(len(terms)):
            term = terms[idx]
            v += term[j] if j < len(term) else ''

        values.append(v)
    

    for v in values:
        if v.strip() == '':
            continue
        v = int(v)
        if op == '*':
            res = res * v
        if op == '+':
            res += v
    tot += res
print('Part 2:', tot)

t2 = perf_counter()
print('Time:', t2 - t1)
