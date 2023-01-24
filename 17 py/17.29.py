a = []
for x in range(2807,8558):
    b = str(bin(x))
    if (b[-1]=="1" and b[-2]=='1') and x%9==5:
        a.append(x)
print(max(a), sum(a))
