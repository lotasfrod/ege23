for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (y + 2*x  <a ) or (x>15) or (y>30):
                k += 1
    if k == 90_000:
        print(a)
        break