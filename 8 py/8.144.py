from itertools import product

el = list(map(''.join, product('АЗИМУТ', repeat = 6)))

c = set()
for i in range(len(el)-1):
    if el[i].count('А')+ el[i].count('И')+ el[i].count('У')>=3:
        c.add(el[i])

print(len(c))