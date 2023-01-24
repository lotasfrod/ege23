print("Задача 19")
def f(x,p):
    if x>=30 or p>3:
        return p==3
    else:
        if p%2==0:
            return f(x+2,p+1) or f(x+3,p+1) or f(x*2,p+1)
        else:
            return f(x+2,p+1) and f(x+3,p+1) and f(x*2,p+1)
    
for i in range(1,30):
    if f(i,1):
        print(i)
        break

print("Задача 20")
def f(x,p):
    if x>=30 or p>4:
        return p==4
    else:
        if p%2!=0:
            return f(x+2,p+1) or f(x+3,p+1) or f(x*2,p+1)
        else:
            return f(x+2,p+1) or f(x+3,p+1) or f(x*2,p+1)
    
for i in range(1,30):
    if f(i,1):
        print(i)
        break

print("Задача 21")
def f(x,p):
    if x>=30 or p>5:
        return p==3 or p==5
    else:
        if p%2==0:
            return f(x+2,p+1) or f(x+3,p+1) or f(x*2,p+1)
        else:
            return f(x+2,p+1) and f(x+3,p+1) and f(x*2,p+1)
    
for i in range(1,30):
    if f(i,1):
        print(i)
        
        







