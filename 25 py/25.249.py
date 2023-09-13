

for i in range(1204065,10**8):
    n=str(i)
    if n[0:2]=='12' and n[-1]=='5' and n[-2]=='6' and n[-4]=='4' and i%161==0:
        print(i,i//161)

