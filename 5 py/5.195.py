for x in range(13):
    b= bin(x)[2::]
    ri = b
    s=0
    while s!=2:
        if b.count('1')%2!=0:
            ri+='1'
            s+=1
        
        else:
            ri+='0'
            s+=1
        
    print(int(ri,2)) 
       








