with open('X:\\информатика\\задачи 24\\24-230.txt') as t:
    t = t.readline()

t = t.split('ZZ')

max1 = 0

for i in t:
    if i[4:6]=='54' and i[9:11]=='22' and len(i)==11:
        max1 = max(max1,int(i))



c = 1
for i in str(max1):
    if int(i)%2!=0:
        c*=int(i)
print(c)
