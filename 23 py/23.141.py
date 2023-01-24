def t(n):
    s = ''
    while n != 0: 
        s += str(n % 3)
        n //= 3
    return s[::-1]
print(t(10))