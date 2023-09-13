c=[]
for i in range(123407,10**8):
    if i%141==0:
        c.append(i)

for k in c:
    x = str(k)
    if x[0:4]=='1234' and x[-1]=='7':
        print(k,k//141)

