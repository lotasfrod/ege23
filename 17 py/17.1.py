a = []
for x in range(2568, 7859):
    if (x%4==0 or x%5==0):
        if x%11!=0 and x%20!=0 and x%27!=0:
            a.append(x)
print(min(a), max(a))