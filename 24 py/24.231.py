with open('X:\\информатика\\задачи 24\\24-230.txt') as t:
     t=t.readline()
t = t.split('K')


max1 = 0

for x in t:
    if x[0:2]=='43' and x[4:6]=='78' and x[9:11]=='34' and len(x)==11:
            max1 = max(max1,int(x))

c = 1
for j in str(max1):
      if int(j)%2!=0:
            c*=int(j)
print(c)




