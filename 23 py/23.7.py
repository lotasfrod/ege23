def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    else:
        return f(x+1,y)+f(x+2,y)
print(f(1,7)*f(7,12))