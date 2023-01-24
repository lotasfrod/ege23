a=[]
c=0
for x in range(2495,7083):
    b = hex(x)[2::]
    if  (b[-1]=='a' and b[-2]=='1') or (b[-1]=='f' and b[-2]=='1'):
        if x%5!=0 and x%9!=0:
            a.append(x)
            c+=1
print(c, min(a))