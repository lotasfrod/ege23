a = []
for x in range(1,1000):
    b = bin(x)[2:]
    b1 = list(map(int,str(b)))
    if x%2==0:
        b=b+'0'
        if b.count('1')>b.count('0'):
            b=b+'0'
            
        else:
            b=b+'1'
           
    else:
        b=b+'1'
        if b.count('1')>b.count('0'):
            b=b+'0'
            
        else:
            b=b+'1'
            
    if 50<(int(b,2))<80:
        a.append(int(b,2))
print(len(a))

