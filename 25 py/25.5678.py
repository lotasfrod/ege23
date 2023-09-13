def suma(n):
    s = 0
    for cif in n:
        if cif in '13579':
            s+=int(cif)
    return s

for i in range(1,10**8+1):
    n=str(i)
    if n[0:3]=='124' and n[-2::]=='79' and '5' in n:
        if i%suma(n) ==0:
            print(i, sum(list(map(int,n)))) 