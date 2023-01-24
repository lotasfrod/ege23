a = []
c = 0
for x in range(3439,7410):
    if ((hex(x)[::-1])!=(bin(x)[::-1]))  and (x%9==0 or x%10==0 or x%11==0):
        a.append(x)
        c+=1
print(c, max(a))
    
