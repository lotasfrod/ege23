from itertools import product
el = list(map(''.join, product('ВОРОБЕЙ',repeat=5)))
m = 'ЕЙ', 'ЙЕ'
c=set()
for i in range(len(el)):
    if (el[i][0])!='Й' and (el[i][-1])!='Й' and el[i].count('Й')<=1 and (not('ЕЙ' in el[i])) and (not('ЙЕ' in el[i])):
        c.add(el[i])
print(len(c))