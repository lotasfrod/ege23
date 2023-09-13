from itertools import permutations

el = list(map(''.join, permutations('КОМЕТА')))
v1='КМТ'
v2 = 'ОЕА'
c = 0


for e in el:
    flag = True
    for i in range(len(e)-1):
        if (e[i] in v1 and e[i+1] in v1) or (e[i+1] in v2 and e[i] in v2):
            flag = False
    if flag:
        c+=1
        
       
print(c)


