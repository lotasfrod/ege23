def f(x):
    b = set()
    for i in range(1, int(x**0.5) +1):
        if x %i==0:
            b.add(i)
            b.add(x//i)
    return sorted(b,reverse = True)


for num in range(190061, 190080 +1):
    delit = f(num)
    count = 0
    chet =[]
    for d in delit:
        if d%2!=0:
            count +=1
        else:
            chet.append(d)
    if count == 4:
        for ch in chet:
            delit.remove(ch)
        print(*delit)