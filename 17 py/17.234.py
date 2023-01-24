el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-1.txt').readlines()))




s = sum(el)/len(el)
a = []
for i in range(len(el)-1):
   
   
    z,x,c = el[i], el[i+1], el[i+2]
    z1,x1,c1 = list(map(int,str(el[i]))), list(map(int,str(el[i+1]))), list(map(int,str(el[i+2])))
    if (9 in z1) and (9 in x1) and (9 in c1):
        if z<s or x<s or c<s:
            a.append(z+x+c)
print(len(a), max(a))