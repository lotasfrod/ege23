print("Задача 19")
def f(x,p):
    if x>=103 or p>3:
        return p == 3
    else:
        if p%2==0:
            return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
        else:
            return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)

for s in range(1,103):
    if f(s,1):
        print(s)
        break


print("Задача 20")
def f(x,p):
    if x>=101 or p>4:
        return p == 4
    if p%2!=0:
        return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
    else:
        return f(x+1,p+1) and f(x+2,p+1) and f(x*2,p+1)

for s in range(1,101):
    if f(s,1):
        print(s)
        

print("Задача 21")
def f(x,p):
    if x>=101 or p>5:
        return p == 5 or p == 3
    else:
        if p%2==0:
            return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
        else:
            return f(x+1,p+1) and f(x+2,p+1) and f(x*2,p+1)

for s in range(1,101):
    if f(s,1):
        print(s)
        break