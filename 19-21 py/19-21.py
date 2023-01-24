print("Задача 19")
def f(x,p):
    if x>=40 or p>3:
        return p == 3
    else:
        if p%2==0:
            return f(x+1,p+1) or f((x*3)-2,p+1)
        else:
            return f(x+1,p+1) or f((x*3)-2,p+1)
for s in range (1,40):
    if f(s,1):
        print(s)
        break


print("Задача 20")
def f(x,p):
    if x>=40 or p>4:
        return p == 4
    else:
        if p%2!=0:
            return f(x+1,p+1) or f((x*3)-2,p+1)
        else:
            return f(x+1,p+1) and f((x*3)-2,p+1)
for s in range (1,40):
    if f(s,1):
        print(s)



print("Задача 21")
def f(x,p):
    if x>=40 or p>5:
        return p == 3 or p==5
    else:
        if p%2==0:
            return f(x+1,p+1) or f((x*3)-2,p+1)
        else:
            return f(x+1,p+1) and f((x*3)-2,p+1)
for s in range (1,40):
    if f(s,1):
        print(s)
        break