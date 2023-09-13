def base(d):
    s = ''
    while d:
        s=str(d%9)+s
        d//=9
    return s
def void(l):
    if l[0] in ['3','7']: return False
    for h in range(9):
        if (str(h)+str(h)) in l:
            return False
    return True
c=0
for i in range( int('1000000',9), int('10000000',9) ):

    if void(base(i)):
        c+=1
print(c)



