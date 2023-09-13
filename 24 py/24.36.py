el = open("E:\\информатика\\задачи 24\\k7c-4.txt").readline()

c = 0

for i in range(len(el)-2):
    x,y,z = el[i], el[i+1], el[i+2]
    if x in 'ADF' and y in 'CDF' and z in 'CDF' and x!=z and y!=z:
        c+=1
print(c)