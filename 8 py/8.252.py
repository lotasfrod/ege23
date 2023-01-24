from itertools import product
s = list(map(''.join, product('ЕГЭИНФ', repeat = 6)))
i = []
for x in range(len(s)):
    if (s[x][0]=='Е') and (s[x][-1] in 'ЭИ') and (s[x].count('ФИ')==2) and not('ЕГЭ' in s[x]):
        i.append(s[x])
print(len(i))