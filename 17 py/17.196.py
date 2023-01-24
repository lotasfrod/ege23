el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-10.txt').readlines()))


a = 0
c = 0


for x in range(len(el)-2):
    x,y,z = el[x], el[x+1], el[x+2]
    if ((x**2)+(y**2)==(z**2)) or ((z**2)+(y**2)==(x**2)) or ((x**2)+(z**2)==(y**2)):
        c+=1
        a+=(max(x,y,z))
print(c, a)


