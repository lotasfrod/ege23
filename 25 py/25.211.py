
for i in range(16):
    for j in range(16):
        num = '1'+str(hex(i))[2::]+'ded'+str(hex(j))[2::]+'ced'
        if int(num,16)%121==0:
            print(int(num,16), int(num,16)//121)