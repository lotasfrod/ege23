
c = 10**10
answer = 0
for l in range(101,1000):
    x = l*'3'
    while '111' in x or '333' in x:
        if '111' in x:
            x = x.replace('111','3',1)
        else:
            x = x.replace('333','1',1)
    if int(x)<c:
        c = int(x)
        answer = l
print(answer)


