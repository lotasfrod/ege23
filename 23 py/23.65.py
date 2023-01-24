def f(x,y):
    if x==y:
        return 1
    if x>y or x==10:
        return 0
    else:
        return  f(x+1,y) + f(x+5,y)
print(f(2,15)*f(15,26))