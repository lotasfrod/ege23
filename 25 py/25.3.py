for n in range(154026, 154044):
    a=[]
    for d in range(1,n//2+1):
        if n%d==0:
            a.append(d)
            if len(a)>3:
                break
    if len(a)==3:
        a.append(n)
        print(*a)