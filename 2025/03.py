print(chr(27)+'[2j')
print('\033c')
f = open('03.test', 'r')
f = open('03.input', 'r')
lines = [x.strip() for x in f.readlines()]

from functools import cache

call = 0

@cache
def largest(line, level):
    global call
    #call += 1
    # if call % 1000000 == 0:
        # print(f'Call: {call}')
    #print(line, level)
    if level == 0 or len(line)==0:
        return ''

    max_nbr = ''
    max_value = 0
    for i,x in enumerate(line):
        test = x + largest(line[i+1:], level - 1)
        value = int(test)
        if value > max_value:
            max_nbr = test
            max_value = value
    return max_nbr



tot1 = 0
tot2 = 0
for line in lines:
    r1 = largest(line, 2)
    #print(f'{line} =>>> {r1}')
    r2 = largest(line, 12)
    #print(f'{line} =>>> {r2}')
    tot1 += int(r1)
    tot2 += int(r2)

print(f'Part 1: {tot1}')
print(f'Part 2: {tot2}')





# tot = 0
# for line in lines:
#     r1 = largest(line, 2)
#     r2 = largest(line, 12)
#     
#     max_nbr = 0
#     for i,x in enumerate(line):
#         for j,y in enumerate(line[i+1:]):
#             nbr = int(x + y)
#             max_nbr = max_nbr if max_nbr > nbr else nbr
#     tot += max_nbr
# 
#     print(f'{line} =>>> {max_nbr}')
# print(f'{tot}')





