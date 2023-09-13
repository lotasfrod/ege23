def f(x,y,z):
    if x==y:
        return z==1
    if x>y or z>1:
        return 0
    if x%2!=0:
        z+=1
    if x<y:
        return f(x+1,y,z) + f(x+2,y,z) + f(x*2,y,z)
    
print(f(2,40,0))
