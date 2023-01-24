for x in range(37):
    f = 5*37**3+(2+x)*37**2+8*37+9+x
    if f%36==0:
        print(f//36)
        break