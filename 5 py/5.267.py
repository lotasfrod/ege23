for x in range(2,1000):
    
    b = bin(x)[2:]
    b1 = bin(x)[3:]
    
    ri = b[0]
    for i in b1:
        ri+='1' if i=='0' else '0'
    ri1 = int(ri,2)
    if x%2!=0 and (x+ri1)>99:
        print(x)
        break










