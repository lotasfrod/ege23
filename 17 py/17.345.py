el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-345.txt').readlines()))

a = []


for o in el:
    if o%100 == 52:
        a.append(o)


answer = max(a)-min(a)
c=0
k = []
for i in range(len(el)-1):
    x,y=el[i], el[i+1]
    if (x<answer) +  (y<answer)==1:
        c+=1
        k.append(x+y)

print(len(k), max(k))


'''end = [x for x in el if x % 100 == 52]
res = []
dif = max(end) - min(end)

for i in range(len(el) - 1):
    if (el[i] < dif) + (el[i+1] < dif) == 1: res.append(el[i] + el[i+1])

print(len(res), max(res))
'''