from itertools import permutations

el = list(map(''.join, permutations('КАБАЛА')))

c = set()

v1 = 'АА'
for i in range(len(el)-1):
    if v1 not in el[i]:
        c.add(el[i])

print(len(c))