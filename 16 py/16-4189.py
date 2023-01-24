def f(n):
    if n==0:
        return 2
    if n>0 and n<=15:
        return f(n-1)
    if n>15 and n<95:
        return 1.6*f(n-3)
    if n>=95:
        return 3.3*f(n-2)
print(f(33))