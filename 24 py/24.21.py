el = open('E:\\информатика\\задачи 24\\k7b-1.txt').readline()
c = 'EAB'
while c in el:
    if c[-1]=='B': c+='E'
    elif c[-1]=='A': c+='B'
    elif c[-1]=='E': c+='A'
print(len(c)-1)