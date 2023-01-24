import re
with open('C:\\Users\\БАТЯ\\Desktop\\информатика\\задачи 24\\\\24-5.txt') as t:
    t = t.read()

t = t.replace('()', '*')
t = re.split('\(|\)', t)



print(len(max(t, key = len)))