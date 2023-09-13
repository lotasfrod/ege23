def un(n):
    m = str(n)
    return d[0]%2==0 and d[1]%2==0 and d[2]%2!=0 and d[3]%2!=0 and d[4]%2!=0 and i%9!=0 and i%13!=0 and i%17!=0
        




mi = 10**10
ma= 0
c = 0
for i in range(64444,77563):
    d = list(map(int,str(i)))
    if un(i):
        c+=1
        ma = max(ma,i)
        mi = min(mi,i)
print(c,ma-mi)    

