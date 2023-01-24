a = []
for x in range(1,750):
    j = bin(x)[2::]
    k = list(map(int,str(j)))
    for i in range(3):
        if (j.count('1') == j.count('0')):
            j = j+ j[-1]
        elif (j.count('1')> j.count('0')):
            j = j+ '0'
        else:
            j = j+ '1'
    o = int(j,2)
    if o%4!=0 and o%2==0:
        a.append(x)
        
print(max(a))
            
        
