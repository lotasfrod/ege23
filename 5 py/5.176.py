a=[]
for x in range(1,1000):
    
    b = bin(x)[2:]
    ri = '1'
    for d in b:
        ri+='1' if d=='0' else '0' 
    if int(ri,2)<=123:
        print(x)

    

    