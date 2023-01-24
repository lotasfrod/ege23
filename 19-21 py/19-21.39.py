def f(x,c,m):
    if x>=25:
        return c%2==m%2
    if c==m:
        return 0
    
    if (c+1)%2==m%2:
        return f(x+2,c+1,m) or f(x*2,c+1,m)
    else:
        return f(x+2,c+1,m) and f(x*2,c+1,m)

for s in range(1,25):
    for m in range(1,5):
        if f(s,0,m)==1:
            print(s,m)
            break

