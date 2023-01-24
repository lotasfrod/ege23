print("Задача 19")
def f(x,p):
    if x>=37 or p>3:
        return p == 3
    else:
        if p%2==0:
            return f(x//2,p+1) or f(x-2,p+1) or f(x//3,p+1) or  f(x-3,p+1)

            
        else:
            return f(x//2,p+1) or f(x-2,p+1) or f(x//3,p+1) or  f(x-3,p+1)

for s in range(1,38):
    if f(s,1):
        print(s)
        break
