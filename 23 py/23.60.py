
def f(x,y):
    if x==y:
        return 1
    if x>y or x==8:
        return 0
    if x<y:
        return f(x+1,y)+f((x*2),y)
print(f(2,20)*f(20,40))