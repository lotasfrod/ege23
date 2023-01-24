c=set()
for x in range(1000):
    b=bin(x)[2:]
    if x%2==0:
        b = '1'+b+'10'
        
    else:
        b = '11'+b+'0'
        
    if 800<=(int(b,2)) and (int(b,2))<=1500:
        c.add(int(b,2))
print(len(c))

