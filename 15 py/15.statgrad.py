def d(n,m):
    if n%m==0:
        return True
    else:
        return False

for x in range(1,1000):
    k=[]
    for y in range(1,1001):
        for a in range(1,1002):
            if (((108%x==0)<=(x%y!=0)) or (x+y>80) or (a-y>x)):
                k.append(a)
print(k)

'''def d(a):
    for x in range(1,1000):
        for y in range(1,1000):
            if not(((108%x==0)<=(x%y!=0)) or (x+y>80) or (a-y>x)):
                return False
    return True

for a in range(1,1000):
    if d(a):
        print(a)
        break'''