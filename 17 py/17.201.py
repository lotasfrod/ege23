el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-199.txt').readlines()))

c = 0
a = []
b=[]

for x in range(100,1000):
    if x%2!=0:
        b.append(x)


for o in range(len(el)-2):
    x,y,z = el[o],el[o+1],el[o+2]
    if (not(x in b)) and (y in b) and (not(z in b)):
        c+=1
        a.append(x+y+z)

print(c, max(a))
