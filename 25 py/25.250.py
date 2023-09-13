from itertools import product
c=0
def check(n):
    global c
    s=int(n)
    if s%73==0:
        c+=1
        print(s,s//73)



l=0
while c<5:
    for i in product('0123456789', repeat=l):
    
        
        check('12345'+''.join(i)+'76')
        if c==5:
            break
    l+=1
    
   


