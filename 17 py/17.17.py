a = []
c=0
for x in range(1056,7564):
    if (x%3==0 or x%11==0):
        if (x%13!=0 and x%17!=0 and x%19!=0 and x%23!=0):
            a.append(x)
            c+=1
print(c, min(a))