for x in range(10,1000):
    b = bin(x)[2:]
    n = list(map(int,str(b)))
    j = str(n[1])
    l = str(n[-2])
    
    h=b+l+j
    
    if (int(h,2))<=128:
        print(x)
        

