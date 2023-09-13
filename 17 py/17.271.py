el = list(map(int, open('E:\\информатика\\задачи 17\\17-271.txt')))

srz = sum(el)/len(el)

a = 0
c=[]

for i in range(len(el)-1):
    x,y = el[i], el[i+1]
    if abs(x)%10+abs(y)%10==7:
        a+=1
        if x<srz and y<srz:
            c.append(x+y)

print(a, max(c))