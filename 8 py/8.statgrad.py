from itertools import product
s = 'ВЕРОНИКА'
m = list(map(''.join, product(s,repeat=6)))
l = 0

for i in range(len(m)):
    if ((m[i].count('В'))+(m[i].count('Р'))+(m[i].count('Н'))+(m[i].count('К')))>((m[i].count('Е'))+(m[i].count('О'))+(m[i].count('И'))+(m[i].count('А'))):
        l+=1
print(l)
