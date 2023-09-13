n  = 96
s = '0'+'1'*(n//2)+'2'*(n//2)+'0'
while '00' not in s:
    s = s.replace('011','20',1)
    s = s.replace('022','10',1)
    s = s.replace('02','110',1)
    s = s.replace('01','220',1)


print(s.count('1'), s.count('2'))