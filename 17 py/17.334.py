el = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-1.txt').readlines()))

p=[]
for o in el:
    if o>0 and o%15==0:
        p.append(o)
min1 = min(p)
a = []
c = 0
for i in range(len(el)-2):
    x,y = el[i],el[i+1]
    if (x%2!=0) and (y%2!=0):
        if ((x+y)//2) >= min1:

        
            c+=1
            a.append(((x+y)//2))

print(c, min(a))
