def fiv(i):
    s = ''
    while i>0:
        r = str(i%5)
        i//=5
        s+=r
    return s[::-1]
        

a = []
for x in range(1000,70000):
    o = str(hex(x))[2::]
    b = list(map(str,oct(x)))
    l = list(map(str,fiv(x)))
    if len(b)==5 and len(l)==6:
        if (o[-1]=='a' and o[-2]=='f'):
            a.append(x)
    
print(a)

    