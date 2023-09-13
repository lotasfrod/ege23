
for i in range(16606,10**6):
    x = str(i)
    c=[]
    if x[1]=='6' and x[-1]=='6' and '6' in x[2:-2] and i%6==0 and i%7==0 and i%8==0:
        for n in range(1,i+1):
            if i%n==0:
                c.append(n)
        print(i,sum(c))

