a = []
c=0
for x in range(1045,8963):
    if (x%5==0 or x%7==0):
        if x%11!=0 and x%13!=0 and x%17!=0 and x%19!=0:
            a.append(x)
            c+=1
print(c, min(a))