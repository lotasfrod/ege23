el = open('E:\\информатика\\задачи 24\\k8-4.txt').readline()

stroka = el[0]
a= []
max1 = 0
for i in range(len(el)-1):
    if el[i]==el[i+1]:
        stroka+=el[i+1]
    else:
        if len(stroka)>=max1:
            max1 = len(stroka)
            a.append(stroka)
        stroka = el[i+1]

if el[-1]==el[-2]:
    if len(stroka)>=max1:
        max1 = len(stroka)
        a.append(stroka)

for x in a:
    if len(x)==max:
        print(x[0], max1)

print(stroka)


