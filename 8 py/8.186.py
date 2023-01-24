from itertools import product
el = list(map(''.join, product('БАЛОН', repeat = 6)))
c=0
for i in range(len(el)):
    if el[i].count('А')<=1 and el[i].count('О')<=1:
        c+=1
print(c)