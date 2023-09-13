el = list(map(int, open('X:\\информатика\\задачи 17\\17-243.txt')))

c=[]
for i in range(len(el)):
    if el[i]%171==0:
        c.append(el[i])
max1 = max(c)


ans = []

for j in range(len(el)-1):
    if (el[j]<max1 or el[j+1]<max1) and (el[j]%2!=0 or el[j+1]%2!=0):
        ans.append(el[j]+el[j+1])

print(len(ans), max(ans))

























'''c = []
for i in range(len(el)):
    if el[i]%171 == 0:
        c.append(el[i])

max1 = max(c)
counter = 0
answer = []
for x in range(len(el)-2):
    z,v = el[x], el[x+1]
    if (z<max1 or v<max1):
        if (z%2!=0 or v%2!=0):
            counter+=1
            answer.append(el[x])

print(counter, max(answer))'''
