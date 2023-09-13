'''for i in range(3850000,3860000):
    m=''
    d = [x for x in range(1,i//2+1) if i%x==0]
    for o in d:
        c=0
        for n in range(1,o+1):
        
            if o%n==0:
                c+=1
        if c==2:
            m+=str(i)
    
    if m[0:2]=='27' and m[-1]=='1' and m[-3]=='1':
        print(i,m)  '''


def f(n):
    m = str(n)
    return m[0:2]=='27' and m[-1]=='1' and m[-3]=='1'

def l(o):
    m=''
    d = [x for x in range(1,o//2+1) if o%x==0]
    for i in d:
        c=0
        for n in range(1,i+1):
        
            if i%n==0:
                c+=1
        if c==2:
            m+=str(i)
    if m>'270101':
        return m
s =[]
for i in range(3850000,3853000):
    if l(i):
       if f(i):
           print(i)



        





    
