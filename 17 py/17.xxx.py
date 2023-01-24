f = open('C:\\Users\\БАТЯ\\Downloads\\17.txt')
    
l = [int(i) for i in f]
c=m =0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i] - l[j]) % 2 == 0 and (l[i] % 19 == 0 or l[j] % 19 == 0):
            c+=1
            m = max(m,l[i]+l[j])

print(c,m)
