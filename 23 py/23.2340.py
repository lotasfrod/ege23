def f(x,y,z):
    if x==y and z==7:
        return 1
    if x>y:
        return 0
    
    else:
        return f(x+1,y,z+1) +f(x+4,y,z+1) + f(x*2,y,z+1)
print(f(3,27,0))