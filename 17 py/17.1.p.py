a = []
c=0
for x in range(1012,9638):
    if x%3==0 and x%11!=0 and x%13!=0 and x%17!=0 and x%19!=0:
        a.append(x)
        c+=1

print(c, max(a))