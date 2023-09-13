
'''el = open('X:\\информатика\\задачи 24\\k7-0.txt').readline()


el = el.replace('A',' ').replace('B',' ')
m = max(el.split(), key=len)
print(len(max(el.split(), key=len)))'''

import re 
with open('X:\\информатика\\задачи 24\\k7-0.txt') as sym:
    print(len(max(re.split('A|B', sym.read(), key=len))))
