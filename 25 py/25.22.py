for n in range(190201, 190281):
    a = []
    for d in range(1,n//2+1):
        if n%d==0 and d%2==0:
            a.append(d)
            if len(a)>3:
                break
    if len(a)==3:
        a.append(n)
        a.reverse()
        print(*a)