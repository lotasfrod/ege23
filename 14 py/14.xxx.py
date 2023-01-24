for num in range(15):
    a = list(reversed([1,2,3,num,5]))
    b = list(reversed([1,num,2,3,3]))
    for i in range(5):
        a[i] = a[i]*15**i
        b[i] = b[i]*15**i
    if (sum(a)+sum(b))%14==0:
        print((sum(a)+ sum(b))//14)
        break