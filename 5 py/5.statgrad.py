def sum_nums(k):
    k = str(int(k,2))
    l = list(map(int, list(k)))
    return sum(l)

def trans(N):
    b = bin(N)[2::]
    for x in range(3):
        if sum_nums(k)%2==0:
            n+='0'
        else:
            n+='1'

    return int(n,2)

m=10**10
for x in range(1,1000):
    if trans(x)>2054:
        m = min(m,trans(x))
print(m)
        