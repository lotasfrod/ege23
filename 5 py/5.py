for i in range(1,10000):
    b = bin(i)[2::]
    b = b.replace('1', '2').replace('0','1').replace('2','0')
    r = int(b,2)
    res = i-r
    if res == 999:
        print(i)
