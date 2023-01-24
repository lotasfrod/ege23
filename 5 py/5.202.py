'''for n in range(1,1000):
    b = bin(n)[2:]
    d = b
    s=0
    while s!=2:
        if n%2==0:
            d+='0'
            s+=1
        else:
            d+='1'
            s+=1
    if (int(d,2))>100:
        print(n)'''

c = 102
l = bin(c)[2::]

b= str(int(l) - int(int(l)%100))
print(c)
print(int(b,2))
