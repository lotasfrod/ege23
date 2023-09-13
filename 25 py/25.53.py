def prost(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
c=0
for i in range(3614033, 3614116):
    if prost(i):
        c+=1
        print(c,i)