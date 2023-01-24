el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-205.txt').readlines()))

a = []
c = 0

for i in range(len(el)-1):
    x,y = el[i], el[i-1]
    if x%7==0 or y%7==0:
        if (x+y)%5==0:
            c+=1
            a.append(x+y)
print(c, max(a))
