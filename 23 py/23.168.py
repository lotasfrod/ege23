def f(x,y):
    if y==10:
        return x==1
    
    
    return f(x+4,y+1)+f(x+7,y+1)+f(x//2,y+1)
print(f(1,0))

