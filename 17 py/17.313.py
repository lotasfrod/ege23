el = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-304.txt').readlines()))

g = []
for o in el:
    if o%321==0:
        g.append(o)

max1 = max(g)

c=0
a=[]
for i in range(len(el)-2):
    x,y = el[i], el[i+1]
    x1, y1 = len(hex(x)), len(hex(y))
    if (x1%2!=0) and (y1%2!=0):
        if x+y<max1:
            c+=1
            a.append(x+y)

print(c, min(a))
