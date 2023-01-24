from itertools import product
el = list(map(''.join, product('ТИМАШЕВСК', repeat = 4)))
c=set()
for i in range(len(el)):
    if (el[i][0]!='Ш') and (el[i][0]!='И') and (el[i][0]!='А') and (el[i][0]!='Е'):
        c.add(el[i])

print(len(c))