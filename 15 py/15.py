for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (3*x + 4*y != 60) or ((a >= x) and (a >= y)):
                k += 1
    if k == 90_000:
        print(a)
        break