print("Задача 19")
def f(x,y,p):
    if x+y>=81 or p>3:
        return p==3
    if p%2==0:
        if x<y:
            return f(x+1, y,p+1) or f(x+2, y, p+1) or f(x*2, y,p+1)
        if x>y:
            return f(x, y+1,p+1) or f(x, y+2, p+1) or f(x, y*2,p+1)
    else:
        if x<y:
            return f(x+1, y,p+1) and f(x+2, y, p+1) and f(x*2, y,p+1)
        if x>y:
            return f(x, y+1,p+1) and f(x, y+2, p+1) and f(x, y*2,p+1)
for s in range(1,69):
    if f(12,s,1):
        print(s)
        break

print("Задача 20")
def f(x,y,p):
    if x+y>=81 or p>4:
        return p==4
    if p%2!=0:
        if x<y:
            return f(x+1, y,p+1) or f(x+2, y, p+1) or f(x*2, y,p+1)
        if x>y:
            return f(x, y+1,p+1) or f(x, y+2, p+1) or f(x, y*2,p+1)
    else:
        if x<y:
            return f(x+1, y,p+1) and f(x+2, y, p+1) and f(x*2, y,p+1)
        if x>y:
            return f(x, y+1,p+1) and f(x, y+2, p+1) and f(x, y*2,p+1)
for s in range(1,69):
    if f(12,s,1):
        print(s)

print("Задача 21")
def f(x,y,p):
    if x+y>=81 or p>5:
        return p==3 or p==5
    if p%2==0:
        if x<y:
            return f(x+1, y,p+1) or f(x+2, y, p+1) or f(x*2, y,p+1)
        if x>y:
            return f(x, y+1,p+1) or f(x, y+2, p+1) or f(x, y*2,p+1)
    else:
        if x<y:
            return f(x+1, y,p+1) and f(x+2, y, p+1) and f(x*2, y,p+1)
        if x>y:
            return f(x, y+1,p+1) and f(x, y+2, p+1) and f(x, y*2,p+1)
for s in range(1,69):
    if f(12,s,1):
        print(s)
        break


