el =open('E:\\информатика\\задачи 24\\k7c-2.txt').readline()
    

c=0
c1 = 'ACE'
c2='ADF'
c3 = 'ABF'

for i in range(len(el)-2):
    x,y,z = el[i], el[i+1], el[i+2]
    if x in c1 and y in c2 and z in c3 and x!=y and y!=z:
            c+=1
print(c)


