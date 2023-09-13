k=0
for i in range(1532160,1532040,-1 ):
    c=2
    for n in range(1,i//2+1):
        if i%n==0:
            c=0
            break
    if c==2:
        k+=1
        print(k,i)