for n in range(2943444, 2943530):
    a=[]
    for d in range(1,round(n**0.5)+1):
        if n%d==0:
            a.append(d)
            if len(a)>1:
                break
    if len(a)==1:
        a.append(n)
        print(*a)