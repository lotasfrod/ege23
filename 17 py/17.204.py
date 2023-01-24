el = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-204.txt').readlines()))

c = 0
a = []
b = []
for o in range(-10000,10000):
    if o>0:
        if o%10==9:
            b.append(o)

for i in range(len(el)-2):
    x,y,z = el[i], el[i+1], el[i+2]
    if (not(x in b)) and (y in b) and (not(z in b)):
        a.append(x+y+z)
        c+=1
print(c, max(a))
