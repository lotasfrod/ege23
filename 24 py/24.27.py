el = open('E:\\информатика\\задачи 24\\k7b-1.txt').readline()
el = el.replace('C', ' ').replace('D', ' ')
m = max(el.split(), key = len)
print(len(m))