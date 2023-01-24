for x in range(1,1000):
    b=bin(x)[2:]
    if x%2==0:
        b=b+'10'
    else:
        b='1'+b+'01'
    if (int(b,2))>516:
        print(x)
        break