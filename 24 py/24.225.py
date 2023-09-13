with open('X:\\информатика\\задачи 24\\24-225.txt') as t:
    t = t.readline()
t = t.split('F')

max1 = 0
for x in t:
    if x[0:2]=='44' and x[4:6]=='78' and x[-1]=='3' and len(x)==10:
        max1 = max(max1, int(x))

c = 0
for i in str(max1):
    if i in '2468':
        c+=int(i)
print(c)



