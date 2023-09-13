with open('X:\\информатика\\задачи 24\\24-225.txt') as t:
    t = t.readline()

el = t.split('RR')

max1 = 0
for i in el:
    if i[0:3]=='322' and i[5:7]=='55' and i[-1]=='9' and i[-2]=='8' and len(i)==12:
        max1 = max(max1,int(i))

c = 0
b = 1
for i in str(max1):
    if int(i)%2==0:
        c+=int(i)
    if int(i)%2!=0:
        b*=int(i)

print(c+b)
