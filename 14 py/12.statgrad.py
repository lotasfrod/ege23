for n in range(1,100):
    s = '0'+10*'1'+10*'2'+'3'*3
    while '00' not in s:
        s = s.replace('012', '30',1)
        if '011' in s:
            s = s.replace('011', '20',1) 
            s = s.replace('022', '40',1) 
        else:
            s = s.replace('01', '10',1) 
            s = s.replace('02', '101',1) 
    '''if s.count('1')==7 and s.count('2')==5:
    print(n)'''
    print(s)