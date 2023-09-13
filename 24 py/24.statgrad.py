'''el = open('C:\\Users\\БАТЯ\\Desktop\\24.txt').readline()


stroka = 0
c=[]
max1=0
a=[]
for i in range(len(el)-1):
    c=0
    if el[i]=='F':
        stroka = el[i]
        while el[i+1]!='F':
            stroka+=el[i+1]
            if el[i+1]=='A':
                c+=1
            if c==2:
                stroka = 0
    else:
        if len(stroka)>=max1:
            max1 = len(stroka)
            a.append(stroka)
        stroka = el[i+1]

print(max1)'''

s, = open('C:\\Users\\БАТЯ\\Desktop\\24.txt')
idx_F = [k for k, v in enumerate(s) if v == 'F']
max_str = max([n[1] - n[0] + 1 for n in zip(idx_F, idx_F[1:]) if s[n[0]:n[1]].count('A') < 3])
print(max_str)