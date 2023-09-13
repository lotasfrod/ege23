for n in range(164700,164753):
    a=[]
    for d in range(1,n//2+1):
        if n%d==0:
            a.append(d)
            if len(a)>5:
                break
    if len(a)==5:
        a.append(n)
        print(*a)