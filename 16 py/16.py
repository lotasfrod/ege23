def f(n):
    if n == 0:
        return 1
    if n==1:
        return 3
    if n%2==0:
        return f(n-1)-f(n-2)+3*n
    if n%2!=0:
        return f(n-2) - f(n-3)+2*n
print(f(40))
