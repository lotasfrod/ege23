def f(x,y,c):
    
    if x==y and c==0:
        return 1
        
    if x>y:
        return 0
    else:
        return f(x+1,y,c-1)+f(x+2,y,c-1)+f(x+3,y,c-1)
print(f(3,22,7))
