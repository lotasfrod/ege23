'''def suma(n):
    delits=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            delits.add(i)
            delits.add(n//i)
    return sum(delits)'''


c=0
for i in range(16616,10**6):
    if i%168==0:
        n = str(i)
        
        if n[1]=='6' and n[-1]=='6' and '6' in n[2:len(n)-1]:
            c+=1
            d=[x for x in range(1,i+1) if i%x==0]
            print(i,sum(d))
    if c==7:
        break