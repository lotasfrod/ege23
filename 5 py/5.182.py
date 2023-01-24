for x  in range(256):
    l = bin(x-1)[2:].zfill(8)
    ri = ''
    for d in l:
        ri+='1' if d=='0' else '0'
    if int(ri,2)==178:
        print(x)