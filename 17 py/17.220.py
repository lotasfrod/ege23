el = list(map(int, open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-1.txt').readlines()))

s = sum(el)/len(el)
a = []
c=0
for i in range(len(el)-1):
    x,y = el[i], el[i+1]
    if (x<s and y>s) or (x>s and y<s):
        a.append(x+y)
        c+=1
print(c, max(a))
