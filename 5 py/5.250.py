i=0
for x in range(60,1000):
    b = bin(x)[2:]
    for i in range(3):
        if b.count("1")==b.count('0'):
            b=b+b[-1]
           
        elif b.count("1")>b.count('0'):
            b=b+'0'
          
        else:
            b=b+'1'
          
    n=int(b,2)
    if n%2==0 and n%4!=0:
        print(x)
        break
    