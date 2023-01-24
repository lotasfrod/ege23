a = []
c=0
for x in range(100,1000):
    
    if x%16==0 and x%3!=0:
        
        a.append(x)
        c+=1
print(sum(a),c)