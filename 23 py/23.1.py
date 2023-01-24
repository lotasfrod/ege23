def f(start, finish):
    if start == finish:
        return 1
    if start>finish:
        return 0
    else:
        return f(start+1, finish) + f(start*2, finish)
print(f(1,16))
        