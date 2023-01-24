from itertools import permutations
s = 'АББАТИСА'
words = set(permutations(s))
count =0 
glas = 'АИ'
sogl = 'БСТ'
for x in words:
    state = True
    for y in range(len(x)-1):
        if (x[y] in glas and x[y+1] in glas) or (x[y] in sogl and x[y+1] in sogl):
            state = False
            break
    if state:
        count+=1
print(count)            

