with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 17\\\\17-4.txt') as t:
    t = t.read()

t = t.replace('\n',',')
print(t)

c = list(t)
print(c)
#a = []
#c = 0
#for x in range(1, len(t)):
#    if int(t[x])%3==0 and int(t[x])%9!=0:
#        if int(t[x][-1::])>=4:
#            c+=1
#            a.append(t[x])



