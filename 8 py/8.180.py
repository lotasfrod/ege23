from itertools import product
el = list(map(''.join, product('МЕЧТА', repeat=6)))
c=0
for i in range(len(el)):
    if el[i].count('А')>=3:
        c+=1
print(c)