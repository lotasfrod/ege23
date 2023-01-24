el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-243.txt').readlines()))

c = []
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

print(counter, max(answer))
