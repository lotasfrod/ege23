def f(s,c,m):
    if s>=37: 
        return c%2==m%2
    if c==m:
        return 0
    
    
    if (c+1)%2==m%2:
        return f(s*3,c+1,m) or f(s*2,c+1,m) or f(s+1,c+1,m)
    else:
        return f(s*3,c+1,m) and f(s*2,c+1,m) and f(s+1,c+1,m)

for s in range(1,36):
    for m in range(1,5):
        if f(s,0,m)==1:
            print(s,m)
            break
