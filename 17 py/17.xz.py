el = list(map(int,open('C:\\Users\\БАТЯ\\Desktop\\17.txt')))
l = []
for k in range(len(el)):
    if el[k]%173==0:
        l.append(el[k])
ma = max(l)

def f(x):
    s=''
    while x>0:
        s=s+str(x%3)
        x//=3
    return s





c = []
for i in range(len(el)-1):
    x,y = el[i], el[i+1]
    if (x>ma or y>ma) and ('22' in f(x) or '22' in f(y)):
        c.append(x+y)

print(len(c), min(c))