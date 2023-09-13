el = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\Доп.файлы\\Задание 17\\17.txt')))

l = []
for o in range(len(el)):
    if abs(el[o])%10==3:
        l.append(el[o])
max1 = max(l)
c=[]
for i in range(len(el)-1):
    x,y = el[i], el[i+1]
    if ((abs(x)%10==3 and abs(y)%10!=3) or (abs(x)%10!=3 and abs(y)%10==3)) and (x**2+y**2)>=max1**2:
        c.append(x**2+y**2)
print(len(c), max(c))
