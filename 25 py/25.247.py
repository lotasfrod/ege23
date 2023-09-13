c=0
now = 700011
while c!=5:
    n=str(now)
    if '1' not in n:
        if n[-4]!='4' and n[-1]!='2':
            state = True
            for i in range(len(n)-3):
                if n[i]=='0' and n[i+3]=='3':
                    state = False
                    break
            if state:
                print(now,sum(list(map(int,n))))
                c+=1
    now+=13