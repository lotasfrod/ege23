el = open('E:\\информатика\\задачи 24\\24-3.txt').readline()
k=0
t = el[0]
for i in range(len(el)-1):
    if el[i]<el[i+1]:
        t+=el[i]
        if len(t)>k:
            k=len(t)
    else:
        t = el[i]
print(k)
