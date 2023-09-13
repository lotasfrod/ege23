k=1
s = 1850000000+k
d = [x for x in range(1,s//2+1) if s%x==0]
c=0
for i in d:
    if i%2==0:
            c+=1
        if c%2!=0:
            print(k,c)

