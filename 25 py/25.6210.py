for i in range(12020,10**7):
    if i%53==0:
        if str(i)==str(i)[::-1]:
            for j in range(0,10):
                if '2'+str(j)+'2' in str(i)[0:len(str(i))]:
                    d = [x for x in range(1,i+1) if i%x==0]
                    if len(d)>30:
                        print(i,sum(d))

