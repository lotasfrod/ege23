el = list(map(int,open('C:\\Users\\БАТЯ\\Downloads\\17_6360.txt')))


l = []
for o in range(len(el)):
    if el[o]%10==7:
        l.append(el[o])
ma = min(l)**2
c=[]
for i in range(len(el)-1):
    x,y = el[i], el[i+1]
    if x%10==y%10 and ((x%7==0 and y%7!=0) or (x%7!=0 and y%7==0)) and x**2+y**2<=ma:
        c.append(x**2+y**2)
print(len(c), max(c))