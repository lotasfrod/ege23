with open('X:\\информатика\\задачи 24\\24-228.txt') as t:
    t = t.readline()
t = t.split('SS')

max1 = 0
for x in t:
    if x[0:2]=='12' and x[6:8]=='77' and x[-1]=='9' and len(x)==11 :
        max1 = max(max1,int(x))


c = 0
b=1
for i in str(max1):
    if int(i)%2!=0:
        c+=int(i)
    if int(i)%2==0:
        b=b*int(i)
print(b+c)
