from itertools import product
el = list(map(''.join, product('СОЛОВЕЙ', repeat=6)))
c=set()

for i in range(len(el)):
    
    if (el[i]).count('Й')<=1 and (el[i][0]!='Й') and (el[i][-1]!='Й') and (not('ЕЙ' in el[i])) and (not('ЙЕ' in el[i])):
        c.add(el[i])
        
print(len(c))