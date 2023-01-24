el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-243.txt').readlines()))


c = []

for o in range(len(el)):
    if el[o]%111 == 0:
        c.append(el[o])

max1 = max(c)

a = []
counter = 0

for i in range(len(el)-1):
    x,y = (el[i]), (el[i+1])
    if (x)>max1 or (y)>max1:
        if x[::-1] == 7:
            a.append(x+y)
            counter+=1

print(counter)
