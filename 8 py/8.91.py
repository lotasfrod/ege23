from itertools import permutations
el = list(map(''.join, permutations('КАЛИЙ')))
c=0
for i in range(len(el)):
    if el[i][0]!='Й' and 'ИА' not in el[i]:
        c+=1
print(c)