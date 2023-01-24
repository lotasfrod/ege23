for x  in range(256):
    l = bin(x)[2:].zfill(8)
    n = int(l)%10
    ri = "" 
    for d in l:
        if d=='0':
            ri+='1'
        else:
            ri+="0"
    if int(ri,2)+n==193:
        print(x)
