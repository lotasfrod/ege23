el = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-282.txt').readlines()))

g=[]
for x in el:
    if x%41==0:
        g.append(x)
max1 = max(g)
print(max1)
c=0
a=[]
for o in range(len(el)-1):
    x,y = el[o], el[o+1]
    if x+y<max1:
        c+=1
        a.append(x+y)
print(c,max(a))
